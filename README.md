# AutoUpdatePACforGFW

因为SSR的作者不再继续开发对程序进行支持了，所以难以在程序里自动更新GFW列表，而万星repo的GFWlist是以Base64加密过的网站列表，解码后也无法直接使用。

由于本人实在太懒了，不想每次都去弄很麻烦，所以现在弄个脚本以后自动去生成最新的pac.txt给SSR使用。

其中GFWlist.txt是来自https://github.com/gfwlist/gfwlist/blob/master/gfwlist.txt 的加密文件，pac.txt是经由脚本生成的为SSR使用的文件，直接放于SSR的文件夹下即可使用。