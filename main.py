import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="公共图书馆数据EDA可视化工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # clean 命令
    subparsers.add_parser("clean", help="执行数据清洗")
    
    # 各个分析命令
    subparsers.add_parser("visits_vs_population", help="绘制人口与访问量散点图")
    subparsers.add_parser("fiscal_year_trends", help="绘制财年趋势折线图")
    subparsers.add_parser("correlations_and_ranking", help="绘制相关性热力图和Top10条形图")
    subparsers.add_parser("visits_by_county", help="绘制按县人均访问量箱线图")
    subparsers.add_parser("user_engagement", help="绘制用户参与度图表")
    
    # all 命令
    subparsers.add_parser("all", help="执行所有分析")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    # 根据命令执行相应操作
    if args.command == "clean":
        from src.data.clean import clean_data
        clean_data()
    
    elif args.command == "visits_vs_population":
        from src.analysis.visits_vs_population import plot_visits_vs_population
        plot_visits_vs_population()
    
    elif args.command == "fiscal_year_trends":
        from src.analysis.fiscal_year_trends import plot_fiscal_year_trends
        plot_fiscal_year_trends()
    
    elif args.command == "correlations_and_ranking":
        from src.analysis.correlations_and_ranking import plot_correlations_and_ranking
        plot_correlations_and_ranking()
    
    elif args.command == "visits_by_county":
        from src.analysis.visits_by_county import plot_visits_by_county
        plot_visits_by_county()
    
    elif args.command == "user_engagement":
        from src.analysis.user_engagement import plot_user_engagement
        plot_user_engagement()
    
    elif args.command == "all":
        print("=== 执行所有分析 ===")
        print("\n--- 1. 数据清洗 ---")
        from src.data.clean import clean_data
        clean_data()
        
        print("\n--- 2. 人口与访问量散点图 ---")
        from src.analysis.visits_vs_population import plot_visits_vs_population
        plot_visits_vs_population()
        
        print("\n--- 3. 财年趋势折线图 ---")
        from src.analysis.fiscal_year_trends import plot_fiscal_year_trends
        plot_fiscal_year_trends()
        
        print("\n--- 4. 相关性热力图和Top10条形图 ---")
        from src.analysis.correlations_and_ranking import plot_correlations_and_ranking
        plot_correlations_and_ranking()
        
        print("\n--- 5. 按县人均访问量箱线图 ---")
        from src.analysis.visits_by_county import plot_visits_by_county
        plot_visits_by_county()
        
        print("\n--- 6. 用户参与度图表 ---")
        from src.analysis.user_engagement import plot_user_engagement
        plot_user_engagement()
        
        print("\n=== 所有分析完成！ ===")

if __name__ == "__main__":
    main()
