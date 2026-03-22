import argparse
import sys

from src.data.clean import clean_data
from src.analysis.visits_vs_population import plot_visits_vs_population
from src.analysis.fiscal_year_trends import plot_fiscal_year_trends
from src.analysis.correlations_and_ranking import plot_correlations_and_ranking
from src.analysis.visits_by_county import plot_visits_by_county
from src.analysis.user_engagement import plot_user_engagement


ANALYSIS_FUNCTIONS = {
    "visits_vs_population": plot_visits_vs_population,
    "fiscal_year_trends": plot_fiscal_year_trends,
    "correlations_and_ranking": plot_correlations_and_ranking,
    "visits_by_county": plot_visits_by_county,
    "user_engagement": plot_user_engagement,
}


def run_all():
    for name, func in ANALYSIS_FUNCTIONS.items():
        print(f"\n{'='*50}")
        print(f"Running: {name}")
        print('='*50)
        func()


def main():
    parser = argparse.ArgumentParser(
        description="Public Libraries Dataset Analysis"
    )
    parser.add_argument(
        "command",
        choices=["clean"] + list(ANALYSIS_FUNCTIONS.keys()) + ["all"],
        help="Command to run: clean, visits_vs_population, fiscal_year_trends, "
             "correlations_and_ranking, visits_by_county, user_engagement, or all"
    )

    args = parser.parse_args()

    if args.command == "clean":
        clean_data()
    elif args.command == "all":
        run_all()
    else:
        ANALYSIS_FUNCTIONS[args.command]()


if __name__ == "__main__":
    main()
