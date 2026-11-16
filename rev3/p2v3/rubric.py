"""Builder's claim-evidence mapping for expert review (review of 015edae, P2-R3).

For every claim that some condition's gold marks as established, state the claim's
quantifier, population and period, what the record shows, and the residual risk the
builder sees. This is NOT validation: the expert fills the verdict columns.
"""

PRACTICE_NOTES = {
    "dev-broiler-density": ("every flock housed at any time in 2025", "records for every flock housed in 2025, cross-checked against invoices; highest recorded density reported",
                            "Density is computed from placement and weight records, not measured continuously; peak density near slaughter is what the limit concerns."),
    "dev-broiler-enrichment": ("every flock placed in 2025, at set-up", "set-up checklists and purchase records for every flock housed in 2025",
                               "Claim narrowed to set-up provision because checklists do not show maintenance through each flock's life."),
    "dev-hen-cagefree": ("all hens kept at any time in 2025", "flock placement records, building registrations and the national register",
                         "Registration shows the housing system type; it does not show conditions within the system."),
    "dev-hen-perch": ("every flock kept in 2025; perch per hen at placement, none removed", "house specifications, installation and maintenance logs, placement numbers",
                      "Perch per hen at placement can only rise as birds are removed; relies on maintenance logs recording any removal."),
    "dev-pig-grouphousing": ("every sow pregnant at any time in 2025, including late-2024 services", "movement, pen and service records from September 2024 to December 2025",
                             "Covers carry-over sows; relies on movement records being complete for stall use."),
    "dev-pig-enrichment": ("every pen, at every daily check in 2025", "complete daily check sheets plus delivery records",
                           "Claim narrowed to what daily checks show; does not establish continuous access between checks."),
}
