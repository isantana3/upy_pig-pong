@REM ampy --port COM5 ls
cd upy_ping-pong
ampy --port COM5 put model
ampy --port COM5 put service
ampy --port COM5 put view
ampy --port COM5 put main.py /main.py
ampy --port COM5 run main.py