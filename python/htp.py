# coding:utf-8

import socket

from multiprocessing import Process
from package import opens
def handle_client(client_socket):
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    newar = str(request_data).split(' ')[1].split('?')[0]
    if(newar.find('.css') != -1):
        response_body = opens({},'html/' + newar)
    elif(newar.find('.png') != -1):
        response_body = str(open('html/' + newar,'rb+').read()) 
    else:
        response_body = opens({},'html/' + newar + '.html')
    # print(request_data)
	# 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    
    # response_body = '123'
    response = response_start_line + response_headers + "\r\n" + response_body
    print(response)
    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()