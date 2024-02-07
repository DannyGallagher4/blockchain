# Start 4 instances of montycoin.py on ports 5000-5003
for ($port = 5000; $port -le 5003; $port++) {
    Start-Process python -ArgumentList ("../montycoin.py", "--port=$port") -NoNewWindow
}
