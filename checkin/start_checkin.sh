kill $(lsof -ti:8000) 2>/dev/null; sleep 1                                                                                                                                 
python -m checkin.api.server &>/tmp/checkin-server.log &                                                  
sleep 2 && curl -s http://localhost:8000/ | grep -o '<title>[^<]*</title>'