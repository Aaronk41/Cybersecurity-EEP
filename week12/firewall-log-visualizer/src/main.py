from parser import parse_logs
from analyzer import analyze_logs
from visualizer import generate_report

if __name__ == "__main__":
    log_path = "logs/sample_logs.txt"
    df = parse_logs(log_path)
    stats = analyze_logs(df)
    generate_report(df, stats)
