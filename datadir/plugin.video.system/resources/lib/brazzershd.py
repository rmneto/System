#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 2014 - Anonymous

import xbmcgui,xbmc,xbmcaddon,xbmcplugin
import urllib,urllib2,re,HTMLParser,os,sys,time
import hqqresolver
from resolvers import *

addon_id = 'plugin.video.system'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
down_path = selfAddon.getSetting('download-folder')
mensagemprogresso = xbmcgui.DialogProgress()

def formatString(texto):
        texto = texto.replace("&#8211;","-")
        texto = texto.replace("&#8216;","'")
        texto = texto.replace("&#8217;","'")
        texto = texto.replace("&#038;","&")
        texto = texto.replace("&amp;","&")
        return texto
        

def traducao(texto):
        return selfAddon.getLocalizedString(texto).encode('utf-8')

def brazzershd_mainmenu():
	addDir("Brazzers HD",'-',202,artfolder + 'videos.png')
	addDir("Category",'-',203,artfolder + 'videos.png')
	addDir("Pornstar",'-',204,artfolder + 'videos.png')
	addDir("Search",'-',205,artfolder + 'search.png')

	xbmc.executebuiltin("Container.SetViewMode(500)")

def brazzershd_menu():
        addLink("[B][COLOR white] BRAZZERS HD [/COLOR][/B]",'','-')

        addDir("Most Recent",'http://brazzershd.net/category/brazzers-hd/?orderby=date',210,artfolder + 'videos.png')
        addDir("Most Viewed",'http://brazzershd.net/category/brazzers-hd/?orderby=views',210,artfolder + 'videos.png')
        addDir("Most Liked",'http://brazzershd.net/category/brazzers-hd/?orderby=likes',210,artfolder + 'videos.png')

        xbmc.executebuiltin("Container.SetViewMode(50)")

def category_menu():
        addLink("[B][COLOR white] CATEGORY [/COLOR][/B]",'','-')

        codigo_fonte = abrir_url('http://brazzershd.net/category/brazzers-hd/?orderby=date')
        codigo_fonte = codigo_fonte.replace("\n","")
        
        match = re.compile('<li id="menu-item(.+?)" class="menu-item menu-item-type-custom menu-item-object-custom(.+?)"><a href="(.+?)">(.+?)</a></li>',flags=0).findall(codigo_fonte)

        a = []
        for x in range(0, len(match)):
                temp = [match[x][2],match[x][3]];
                if len(match[x][2]) > 5: a.append(temp)
        total=len(a)
        for url,titulo in a:
                addDir(titulo,url,210,artfolder + 'videos.png')
                print titulo

        xbmc.executebuiltin("Container.SetViewMode(50)")

def pornstar_menu():
        addLink("[B][COLOR white] PORNSTAR [/COLOR][/B]",'','-')

        codigo_fonte = abrir_url('http://brazzershd.net/category/brazzers-hd/?orderby=date')
        codigo_fonte = codigo_fonte.replace("\n","")
        
        match = re.compile('<li id="menu-item(.+?)" class="menu-item menu-item-type-taxonomy menu-item-object-post_tag(.+?)"><a href="(.+?)">(.+?)</a></li>',flags=0).findall(codigo_fonte)

        a = []
        for x in range(0, len(match)):
                temp = [match[x][2],match[x][3]];
                if len(match[x][2]) > 5: a.append(temp)
        total=len(a)
        for url,titulo in a:
                addDir(titulo,url,210,artfolder + 'videos.png')
                print titulo

        xbmc.executebuiltin("Container.SetViewMode(50)")

#############################################################################################################################
def mode(mode,name,url,iconimage):
        if mode==201: brazzershd_mainmenu()
        elif mode==202: brazzershd_menu()
        elif mode==203: category_menu()
        elif mode==204: pornstar_menu()
        elif mode==205: pesquisa()
        elif mode==210: listar_videos(url)
        elif mode==211: encontrar_fontes(name,url,iconimage)
        
        
def download(name,url):
        if down_path == '':
                dialog = xbmcgui.Dialog()
                dialog.ok(traducao(2010), traducao(2024))
                selfAddon.openSettings()
                return
        #mensagemprogresso.create('Adults TV', traducao(2008),traducao(2009))
        #mensagemprogresso.update(0)
        
        try: video_url = re.compile('<iframe src="(.+?)"').findall(abrir_url(url))[0]
        except: return
        if re.search('urlvk=',video_url): video_url = urllib.unquote(video_url.split('urlvk=')[1])
        if video_url[:2] == '//': video_url = 'http:' + video_url
        url_video = vkcom_resolver(video_url)
        
        name = re.sub('[^-a-zA-Z0-9_.()\\\/ ]+', '',name)
        name += ' - ' + url_video[1] + '.mp4'
        mypath=os.path.join(down_path,name)
        if os.path.isfile(mypath) is True:
                dialog = xbmcgui.Dialog()
                dialog.ok(traducao(2010),traducao(2025))
                return
        #mensagemprogresso.close()
        dp = xbmcgui.DialogProgress()
        dp.create('Download')
        start_time = time.time()                # url - url do ficheiro    mypath - localizacao ex: c:\file.mp3
        try: urllib.urlretrieve(url, mypath, lambda nb, bs, fs: dialogdown(nb, bs, fs, dp, start_time))
        except:
                while os.path.exists(mypath): 
                        try: os.remove(mypath); break 
                        except: pass
                dp.close()
                return
        dp.close()
        
def dialogdown(numblocks, blocksize, filesize, dp, start_time):
      try:
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB %s %.02f MB' % (currently_downloaded,traducao(2026), total) 
            e = ' (%.0f Kb/s) ' % kbps_speed 
            tempo = traducao(2027) + ' %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs + e,tempo)
      except: 
            percent = 100 
            dp.update(percent) 
      if dp.iscanceled(): 
            dp.close()
            raise StopDownloading('Stopped Downloading')

class StopDownloading(Exception):
      def __init__(self, value): self.value = value 
      def __str__(self): return repr(self.value)
          
def cat():
        addLink("[B][COLOR white]CATEGORIES[/COLOR][/B]",'','-')

        codigo_fonte = abrir_url('http://pornohub.su/')
        match = re.compile('<li class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-110">(.+?)</ul></li>').findall(codigo_fonte)
        match2 = re.compile('<a href="(.+?)">(.+?)</a>').findall(match[0])
        for url, titulo in match2:
                addDir(titulo,url,151,artfolder + 'videos.png')
                
        xbmc.executebuiltin("Container.SetViewMode(50)")
        
def listar_videos(url):
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")
        
        codigo_fonte_videos = re.compile('<a class="clip-link"(.+?)</a>',flags=0).findall(codigo_fonte)

        try:
                page = int(re.compile('<span class="current">(.+?)</span>').findall(codigo_fonte)[0])
        except: page = 1

        a = []
        i = 0

        t = url.find("/tag/")
        s = url.find("brazzershd.net/?s=")

        if t>0 or s>0: i=100

        
        for m in codigo_fonte_videos:
                match = re.compile('title="(.+?)" href="(.+?)">.*<img src="(.+?)"').findall(m)
                for x in range(0, len(match)):
                        temp = [match[x][1],match[x][0],match[x][2]];
                        if i > 9 and len(a) < 16 : a.append(temp)
                        #a.append(temp)
                i=i+1
        total=len(a)
        #print 'rui test'
        #print total
        #print codigo_fonte_videos
        for url,titulo,img in a:
                if img[:2] == '//': img = 'http:' + img
                addDir(titulo,url,211,img,False,total,True)
        
        try:
                next_page = re.compile('<span class=\'current\'>(.+?)</span><a class="page larger" href="(http.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                addDir(traducao(2050),url,210,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass
        
        xbmc.executebuiltin("Container.SetViewMode(500)")

        
def encontrar_fontes(name,url,iconimage):
        #url = "http://brazzershd.net/brazzers-hd/hot-cop-mean-cop-2/"
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")

        print 'ruitest'
        iframe_url = re.compile('<iframe src="(.+?)" scrolling="no"').findall(codigo_fonte)
        if len(iframe_url)==0 or iframe_url[0].find(".mp4")>0:
        #if 1==1:
                script_url = re.compile('<div class="screen fluid-width-video-wrapper">.*<script src="(.+?)">.*<script src="(.+?)">').findall(codigo_fonte)[0]
                hash_url = script_url[0]
                iframe_url = script_url[1]
                codigo_fonte = abrir_url(hash_url)
                codigo_fonte = urllib.unquote(codigo_fonte)
                vid = re.compile("var vid = '(.+?)'").findall(codigo_fonte)[0]

                hqqvidresolver = hqqresolver.hqqResolver()
                video_url = hqqvidresolver.resolve(vid)
                print 'video_url: '+video_url
        else:
                if iframe_url[0].find(".mp4") > 0:
                        video_url = iframe_url
                else:
                        codigo_fonte = abrir_url(iframe_url[0])
                        codigo_fonte = codigo_fonte.replace("\n","")
                        sources = re.compile("{file:'(.+?)',label:'(.+?)',type: '(.+?)'}").findall(codigo_fonte)
                        print sources[len(sources)-1][0]
                        video_url = sources[len(sources)-1][0]
                
        print iframe_url
        print video_url

        url_video = urllib.unquote(video_url)
        
        if url_video: play(name,url_video,iconimage)

def listar_categories():
        codigo_fonte = abrir_url('http://brazzershd.net/category/brazzers-hd/?orderby=date')
        codigo_fonte = codigo_fonte.replace("\n","")
        
        match = re.compile('<li id="menu-item(.+?)" class="menu-item(.+?)"><a href="(.+?)">(.+?)</a></li>',flags=0).findall(codigo_fonte)

        a = []
        for x in range(0, len(match)):
                temp = [match[x][2],match[x][3]];
                if len(match[x][2]) > 5: a.append(temp)
        total=len(a)
        for url,titulo in a:
                addDir(titulo,url,210,artfolder + 'videos.png')
                print titulo
        
def play(name,streamurl,iconimage = "DefaultVideo.png"):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        player = xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER)
        player.play(streamurl,listitem)
        
def pesquisa():
        keyb = xbmc.Keyboard('', traducao(2022)+':')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                parametro_pesquisa=urllib.quote(search)
                url = 'http://brazzershd.net/?s=' + str(parametro_pesquisa)
                listar_videos(url)

def abrir_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
                
def addLink(name,url,iconimage):
        name = formatString(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + '/fanart.jpg')
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage,pasta = True,total=1,video=False):
        name = formatString(name)
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + '/fanart.jpg')
        cm =[]
        if video: 
                cm.append(('Download', 'XBMC.RunPlugin(%s?mode=205&url=%s&name=%s)' % (sys.argv[0], urllib.quote_plus(url),name)))
                liz.addContextMenuItems(cm, replaceItems=True) 
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
        return ok
