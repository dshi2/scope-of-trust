"""Figures for a P2 analysis (reads analysis.json from analyze_p2.py; matplotlib).

  python3 plot_p2.py --analysis runs/X/analysis.json [--out runs/X/figures]

fig_p2_forest      P1-P3 (unsupported Q_obs) and P4 (correct acceptance, E_scope - E) per model, in percentage
                   points: equal-case estimate, provisional 95% interval (tango_c_cc on all-pairs counts; line),
                   worst-best scheduled-denominator bounds (grey band), zero line; P4 also marks the one-sided
                   97.5% lower bound (bar tick). Hollow marker = every case difference identical (zero spread).
fig_p2_ladder      evidence ladder: unsupported Q_obs rate by condition (E and E_scope split by direction), per
                   model; rate over all scored trials (no interval: trials are not independent).
fig_p2_validity    validity / positive controls V1-V3 per cell and model: equal-case rate with Wilson 95% interval
                   on n = cases (conservative).
fig_p2_components  component table as small multiples: P1-P3 on unsupported Q_obs, Q_cause, Q_welfare and the
                   Q_obs-or-Q_cause composite (only Q_obs is confirmatory), estimate and provisional 95% interval.
Each figure is written as PNG (200 dpi) and PDF. Titles carry the development / provisional label.
"""
import argparse
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]  # validated categorical slots 1-4 (light surface)
MARKERS = ["o", "s", "^", "D"]  # second encoding: two slots are below 3:1 contrast
INK, MUTED, GRID, BAND = "#222222", "#6b6b6b", "#e6e6e3", "#cfcfca"
PRIMARY = ("P1", "P2", "P3")
NICE_C = {"P1": "P1  B − A\n(audit vs none)", "P2": "P2  B − D1\n(audit vs placebo)",
          "P3": "P3  C − B\n(scope-blind vs audit)", "P4": "P4  E_scope − E\ncorrect acceptance"}
COMPONENTS = ("unsupported_q_obs", "unsupported_q_cause", "unsupported_q_welfare", "unsupported_obs_or_cause")
NICE_COMP = {"unsupported_q_obs": "Q_obs (confirmatory)", "unsupported_q_cause": "Q_cause",
             "unsupported_q_welfare": "Q_welfare", "unsupported_obs_or_cause": "Q_obs or Q_cause"}
LADDER = ["A/none", "A0/none", "B/none", "C/none", "C_prime/none", "D1/none", "D2/none",
          "E/improved", "E/unchanged", "E/worsened",
          "E_scope/improved", "E_scope/unchanged", "E_scope/worsened", "V/none"]
NICE_V = {"V1_correct_acceptance": "V1 correct acceptance", "V2_correct_refutation": "V2 correct refutation",
          "V3_manipulation_check": "V3 manipulation check"}


def style(ax, grid_axis="both"):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(MUTED)
    ax.tick_params(colors=INK, labelsize=8)
    ax.grid(axis=grid_axis, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def save(fig, out, name):
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(out, f"{name}.{ext}"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def pp(v):
    return None if v is None else 100 * v


def offset(j, n, step=0.16):
    """Vertical dodge: first model on top of each row group."""
    return ((n - 1) / 2 - j) * step


def degenerate(o):
    d = o.get("case_differences") or []
    return len(d) > 1 and max(d) - min(d) < 1e-12


def interval_row(ax, y, o, j, label=None, band=None, lower1=None):
    """One model's row: grey bounds band, CI line, estimate marker, optional one-sided lower tick."""
    if band and None not in band:
        ax.plot([pp(min(band)), pp(max(band))], [y, y], color=BAND, linewidth=5, solid_capstyle="butt", zorder=1)
    ci = o.get("ci95")
    if ci:
        ax.plot([pp(ci[0]), pp(ci[1])], [y, y], color=COLORS[j], linewidth=1.6, zorder=2)
    if lower1 is not None:
        ax.plot(pp(lower1), y, marker="|", markersize=13, markeredgewidth=2.2, color=COLORS[j], zorder=3)
    if o.get("estimate") is not None:
        hollow = degenerate(o)
        ax.plot(pp(o["estimate"]), y, MARKERS[j], markersize=7, zorder=4,
                markerfacecolor="white" if hollow else COLORS[j], markeredgecolor=COLORS[j],
                markeredgewidth=1.4, label=label)


def forest(an, models, out, sub):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [3, 2]})
    for ax, names, xl in ((axes[0], PRIMARY, "difference in unsupported Q_obs rate (pp)"),
                          (axes[1], ("P4",), "difference in correct acceptance (pp), E_scope − E")):
        style(ax)
        ax.axvline(0, color=MUTED, linewidth=1, zorder=0)
        for j, m in enumerate(models):
            cs = an["models"][m]["contrasts"]
            for i, n in enumerate(names):
                c = cs.get(n, {})
                o = c.get("observed", {})
                y = len(names) - 1 - i + offset(j, len(models))
                band = (c.get("worst", {}).get("estimate"), c.get("best", {}).get("estimate"))
                interval_row(ax, y, o, j, label=m if i == 0 else None, band=band,
                             lower1=o.get("lower_975_one_sided") if n == "P4" else None)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels([NICE_C[n] for n in reversed(names)], fontsize=8)
        ax.set_ylim(-0.6, len(names) - 0.4)
        ax.set_xlim(-105, 105)
        ax.set_xlabel(xl, fontsize=9, color=INK)
    axes[0].set_title("primary contrasts (positive = more unsupported Q_obs)", fontsize=9, color=INK)
    axes[1].set_title("noninferiority (margin not fixed); | = one-sided 97.5% lower bound", fontsize=9, color=INK)
    h, l = axes[0].get_legend_handles_labels()
    h += [plt.Line2D([], [], color=BAND, linewidth=5), plt.Line2D([], [], marker="o", linestyle="",
          markerfacecolor="white", markeredgecolor=MUTED)]
    l += ["worst–best bounds", "zero spread across cases"]
    fig.legend(h, l, fontsize=8, frameon=False, ncol=len(h), loc="lower center", bbox_to_anchor=(0.5, -0.06))
    fig.suptitle("P2 contrasts per model: estimate, provisional 95% interval (Tango-c-cc, all-pairs counts), "
                 "scheduled-denominator bounds (grey)\n" + sub, fontsize=9, color=INK)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, out, "fig_p2_forest")


def ladder(an, models, out, sub):
    present = set().union(*(an["models"][m]["unsupported_q_obs_rate"] for m in models))
    cells = [c for c in LADDER if c in present] + sorted(present - set(LADDER))
    fig, ax = plt.subplots(figsize=(11, 3.8))
    style(ax, "y")
    groups = [("no outcome audit", [c for c in cells if not c.startswith(("E/", "E_scope/"))]),
              ("E", [c for c in cells if c.startswith("E/")]), ("E_scope", [c for c in cells if c.startswith("E_scope/")])]
    for name, g in groups[1:]:
        if g:
            ax.axvspan(cells.index(g[0]) - 0.45, cells.index(g[-1]) + 0.45, color="#f4f4f1", zorder=0)
    for j, m in enumerate(models):
        r = an["models"][m]["unsupported_q_obs_rate"]
        xs = [i - offset(j, len(models), 0.14) for i in range(len(cells))]
        ys = [r[c]["rate"] if c in r else float("nan") for c in cells]
        ax.plot(xs, ys, MARKERS[j], color=COLORS[j], markersize=7, label=m, linestyle="", zorder=3,
                markeredgecolor="white", markeredgewidth=0.8)
    ax.set_xticks(range(len(cells)))
    short = {"improved": "impr.", "unchanged": "unch.", "worsened": "wors."}
    ax.set_xticklabels([c.replace("/none", "") if "/" not in c.replace("/none", "") else
                        "{}\n{}".format(c.split("/")[0], short.get(c.split("/")[1], c.split("/")[1])) for c in cells],
                       fontsize=8)
    ax.set_ylim(-0.04, 1.04)
    ax.set_xlim(-0.6, len(cells) - 0.4)
    ax.set_ylabel("unsupported Q_obs rate", fontsize=8, color=INK)
    ax.legend(fontsize=8, frameon=False, ncol=len(models), loc="upper center", bbox_to_anchor=(0.5, -0.17))
    ax.set_title("P2 evidence ladder: unsupported Q_obs rate by condition (shaded = outcome-audit arms by "
                 "direction); rate over scored trials, no interval\n" + sub, fontsize=9, color=INK)
    save(fig, out, "fig_p2_ladder")


def validity(an, models, out, sub):
    checks = {}
    for m in models:
        for name, cells in an["models"][m]["validity_checks"].items():
            checks.setdefault(name, [])
            checks[name] += [c for c in cells if c not in checks[name]]
    names = [n for n in NICE_V if n in checks] + sorted(set(checks) - set(NICE_V))
    sizes = [len(checks[n]) for n in names]
    fig, axes = plt.subplots(1, len(names), figsize=(11, 0.45 * max(sizes) + 1.8),
                             gridspec_kw={"width_ratios": [1] * len(names)}, squeeze=False)
    for ax, n in zip(axes[0], names):
        style(ax, "x")
        cells = checks[n]
        for j, m in enumerate(models):
            vc = an["models"][m]["validity_checks"].get(n, {})
            for i, c in enumerate(cells):
                v = vc.get(c)
                if not v or v.get("rate") is None:
                    continue
                y = len(cells) - 1 - i + offset(j, len(models), 0.18)
                ci = v.get("ci95_wilson_cases")
                if ci:
                    ax.plot(ci, [y, y], color=COLORS[j], linewidth=1.6, zorder=2)
                ax.plot(v["rate"], y, MARKERS[j], color=COLORS[j], markersize=7, zorder=3, clip_on=False,
                        markeredgecolor="white", markeredgewidth=0.8, label=m if i == 0 else None)
        ax.set_yticks(range(len(cells)))
        ax.set_yticklabels(list(reversed(cells)), fontsize=8)
        ax.set_ylim(-0.6, len(cells) - 0.4)
        ax.set_xlim(-0.03, 1.03)
        ax.set_xlabel("equal-case rate", fontsize=8, color=INK)
        ax.set_title(NICE_V.get(n, n), fontsize=9, color=INK)
    h, l = axes[0][0].get_legend_handles_labels()
    fig.legend(h, l, fontsize=8, frameon=False, ncol=len(models), loc="lower center", bbox_to_anchor=(0.5, -0.04))
    fig.suptitle("P2 validity and positive controls (must pass before contrasts are read): "
                 "Wilson 95% on n = cases\n" + sub, fontsize=9, color=INK)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, out, "fig_p2_validity")


def components(an, models, out, sub):
    names = [n for n in PRIMARY if any(n in an["models"][m]["components"] for m in models)]
    fig, axes = plt.subplots(1, len(names), figsize=(11, 3.6), sharey=True, squeeze=False)
    for ax, n in zip(axes[0], names):
        style(ax)
        ax.axvline(0, color=MUTED, linewidth=1, zorder=0)
        for j, m in enumerate(models):
            comps = an["models"][m]["components"].get(n, {})
            for i, k in enumerate(COMPONENTS):
                o = comps.get(k)
                if o:
                    interval_row(ax, len(COMPONENTS) - 1 - i + offset(j, len(models)), o, j,
                                 label=m if i == 0 else None)
        ax.axhspan(len(COMPONENTS) - 1.5, len(COMPONENTS) - 0.5, color="#f4f4f1", zorder=0)
        ax.set_yticks(range(len(COMPONENTS)))
        ax.set_yticklabels([NICE_COMP[k] for k in reversed(COMPONENTS)], fontsize=8)
        ax.set_ylim(-0.6, len(COMPONENTS) - 0.4)
        ax.set_xlim(-105, 105)
        ax.set_xlabel("difference in unsupported rate (pp)", fontsize=8, color=INK)
        ax.set_title(NICE_C[n].replace("\n", " "), fontsize=9, color=INK)
    h, l = axes[0][0].get_legend_handles_labels()
    fig.legend(h, l, fontsize=8, frameon=False, ncol=len(models), loc="lower center", bbox_to_anchor=(0.5, -0.05))
    fig.suptitle("P2 components (spec §6; only Q_obs, shaded, is confirmatory): estimate and provisional 95% "
                 "interval\n" + sub, fontsize=9, color=INK)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, out, "fig_p2_components")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--analysis", required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    with open(a.analysis) as f:
        an = json.load(f)
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.analysis)), "figures")
    os.makedirs(out, exist_ok=True)
    models = sorted(an["models"])
    if len(models) > len(COLORS):
        raise SystemExit(f"{len(models)} models; the palette has {len(COLORS)} slots (facet instead)")
    sub = f"{an.get('n_cases', '?')} cases. DEVELOPMENT cases; intervals provisional."
    forest(an, models, out, sub)
    ladder(an, models, out, sub)
    validity(an, models, out, sub)
    components(an, models, out, sub)
    print("wrote", sorted(os.listdir(out)))


if __name__ == "__main__":
    main()
