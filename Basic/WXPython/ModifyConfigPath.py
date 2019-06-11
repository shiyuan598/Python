# encoding:utf-8
import wx
# 参考 https://www.cnblogs.com/morries123/p/8568666.html

class ModifyConfigPath(wx.Frame):
    def __init__(self):
        # frame = wx.Frame(None, title='Modify Config Path', pos=(400, 400), size=(400, 400))
        frame = wx.Frame(None, title='Modify Config Path', pos=(400, 300), size=(400, 400))
        path_text = wx.TextCtrl(frame, pos=(5, 5), size=(260, 24))
        open_button = wx.Button(frame, label="打开", pos=(270, 5), size=(50, 24))
        save_button = wx.Button(frame, label="保存", pos=(330, 5), size=(50, 24))
        content_text = wx.TextCtrl(frame, pos=(5, 35), size=(375, 320),
                               style=wx.TE_MULTILINE)  # wx.TE_MULTILINE可以实现换行功能,若不加此功能文本文档显示为一行显示

        def openfile(event):
            filesFilter = "Txt (*.txt)|*.txt|" "All files (*.*)|*.*"
            fileDialog = wx.FileDialog(None, defaultDir='E:\\code\\00test\\Python\\Basic\\VisitBolg', message="选择单个文件", wildcard=filesFilter, style=wx.FD_OPEN)
            dialogResult = fileDialog.ShowModal()
            if dialogResult != wx.ID_OK:
                return
            path = fileDialog.GetPath()
            path_text.SetValue(path)
            path = path_text.GetValue()
            with open(path, 'r', encoding='utf-8') as f:
                content_text.SetValue(f.read())
        open_button.Bind(wx.EVT_BUTTON, openfile)
        frame.Show()


def main():
    app = wx.App()
    modifyConfigPath = ModifyConfigPath()
    app.MainLoop()


if __name__ == '__main__':
    main()
