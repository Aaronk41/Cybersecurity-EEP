#!/bin/bash

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
log_file="logs/audit_$timestamp.txt"

mkdir -p logs

echo "System Audit Report - $timestamp" > "$log_file"
echo "" >> "$log_file"

echo "Hostname: $(hostname)" >> "$log_file"
echo "Uptime: $(uptime -p)" >> "$log_file"
echo "Current Users: $(who | wc -l)" >> "$log_file"
echo "Logged-in Users:" >> "$log_file"
who >> "$log_file"
echo "" >> "$log_file"

echo "Disk Usage:" >> "$log_file"
df -h >> "$log_file"
echo "" >> "$log_file"

echo "Memory Usage:" >> "$log_file"
free -h >> "$log_file"
echo "" >> "$log_file"

echo "Top Processes:" >> "$log_file"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 10 >> "$log_file"
echo "" >> "$log_file"

echo "Open Ports:" >> "$log_file"
ss -tuln >> "$log_file"
echo "" >> "$log_file"

echo "Failed SSH Logins:" >> "$log_file"
grep "Failed password" /var/log/auth.log 2>/dev/null | wc -l >> "$log_file"
echo "" >> "$log_file"

echo "Audit complete. Report saved to $log_file"
