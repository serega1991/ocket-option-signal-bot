
#!/bin/bash
echo "Deploying Pocket Option Signal Bot..."
pip install -r requirements.txt
python src/signal_bot_twelvedata.py
