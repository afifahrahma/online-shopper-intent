mkdir -p ~/.streamlit/
echo "[theme]
primaryColor= '#6eb52f'
backgroundColor=  '#f0f0f5'
secondaryBackgroundColor= '#F4C2C2'
textColor= '#262730'
font= 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
