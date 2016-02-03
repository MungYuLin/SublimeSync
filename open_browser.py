import sublime, sublime_plugin
import webbrowser

url_map = {
    '/Users/andrew_liu/HTML/' : 'file:///Users/andrew_liu/HTML/',#这里需要进行个人电脑的配置, 配置个人项目路径
}

class OpenBrowserCommand(sublime_plugin.TextCommand):
    def run(self, edit) :
        window = sublime.active_window()
        window.run_command('save')
        url = self.view.file_name()
        flag = False
        for path, domain in url_map.items():
            if url.startswith(path):
                url = url.replace(path, domain).replace('\\', '\/')
                flag = True
                break
        if not flag:
            url = 'file://' + url
        webbrowser.open_new(url) #这里使用默认的浏览器调试
