#!/bin/bash

echo ""
echo "📦 Installing required dependencies..."
pip install -r requirements.txt

echo ""
echo "🚀 Starting the CLI Exam App..."
python3 exam_test.py
