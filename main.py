"""Main entry point for Public Libraries Dataset Analysis."""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.data.clean import clean_data
from src.analysis.visits_vs_population import plot_visits_vs_population
from src.analysis.fiscal_year_trends import plot_fiscal_year_trends
from src.analysis.correlations_and_ranking import plot_correlations_and_ranking
from src.analysis.visits_by_county import plot_visits_by_county
from src.analysis.user_engagement import plot_user_engagement


def run_clean():
    """Run data cleaning."""
    print("Running data cleaning...")
    clean_data()
    print("Data cleaning completed.")


def run_visits_vs_population():
    """Run visits vs population analysis."""
    print("Running visits vs population analysis...")
    plot_visits_vs_population()


def run_fiscal_year_trends():
    """Run fiscal year trends analysis."""
    print("Running fiscal year trends analysis...")
    plot_fiscal_year_trends()


def run_correlations_and_ranking():
    """Run correlations and ranking analysis."""
    print("Running correlations and ranking analysis...")
    plot_correlations_and_ranking()


def run_visits_by_county():
    """Run visits by county analysis."""
    print("Running visits by county analysis...")
    plot_visits_by_county()


def run_user_engagement():
    """Run user engagement analysis."""
    print("Running user engagement analysis...")
    plot_user_engagement()


def run_all():
    """Run all analyses."""
    print("Running all analyses...")
    run_visits_vs_population()
    run_fiscal_year_trends()
    run_correlations_and_ranking()
    run_visits_by_county()
    run_user_engagement()


def main():
    parser = argparse.ArgumentParser(
        description="Public Libraries Dataset Analysis Tool"
    )
    parser.add_argument(
        "command",
        choices=[
            "clean",
            "visits_vs_population",
            "fiscal_year_trends",
            "correlations_and_ranking",
            "visits_by_county",
            "user_engagement",
            "all"
        ],
        help="Command to execute"
    )
    
    args = parser.parse_args()
    
    commands = {
        "clean": run_clean,
        "visits_vs_population": run_visits_vs_population,
        "fiscal_year_trends": run_fiscal_year_trends,
        "correlations_and_ranking": run_correlations_and_ranking,
        "visits_by_county": run_visits_by_county,
        "user_engagement": run_user_engagement,
        "all": run_all
    }
    
    commands[args.command]()


if __name__ == "__main__":
    main()
