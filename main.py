import webview
import os
import sys
 
def resource_path(relative_path):
    """获取打包后资源的绝对路径"""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
 
if __name__ == '__main__':
    html_path = resource_path('index.html')
    webview.create_window('我的应用', 'file://' + html_path)
    webview.start()

