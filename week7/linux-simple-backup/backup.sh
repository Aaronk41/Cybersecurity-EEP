#!/bin/bash

SOURCE_DIRS=("$@")
BACKUP_DIR="backups"
LOG_FILE="backup.log"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

if [ ${#SOURCE_DIRS[@]} -eq 0 ]; then
  echo "Usage: $0 <directory1> <directory2> ..."
  exit 1
fi

ARCHIVE_NAME="backup_$TIMESTAMP.tar.gz"

tar -czf "$BACKUP_DIR/$ARCHIVE_NAME" "${SOURCE_DIRS[@]}"

if [ $? -eq 0 ]; then
  echo "Backup successful: $ARCHIVE_NAME" | tee -a "$LOG_FILE"
else
  echo "Backup failed at $TIMESTAMP" | tee -a "$LOG_FILE"
  exit 1
fi

