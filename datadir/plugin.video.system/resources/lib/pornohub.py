#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 2014 - Anonymous

import xbmcgui,xbmc,xbmcaddon,xbmcplugin
import urllib,urllib2,re,HTMLParser,os,sys,time
from resolvers import *

addon_id = 'plugin.video.system'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
down_path = selfAddon.getSetting('download-folder')
mensagemprogresso = xbmcgui.DialogProgress()

def formatString(texto):
        texto = texto.replace("&#8211;","-")
        texto = texto.replace("&#8217;","'")
        texto = texto.replace("&#038;","&")
        texto = texto.replace("&amp;","&")
        return texto
        

def traducao(texto):
        return selfAddon.getLocalizedString(texto).encode('utf-8')

def pornohub_mainmenu():
	addDir("Networks",'-',140,artfolder + 'videos.png')
	addDir("Pornohub",'-',150,artfolder + 'videos.png')
	addDir("Categories",'-',160,artfolder + 'videos.png')
	addDir("Pornstars",'-',170,artfolder + 'videos.png')
	addDir("Archives",'-',190,artfolder + 'videos.png')
	addDir("Search",'-',180,artfolder + 'search.png')
	#bla_video('bla','bla','bla','bla')
	xbmc.executebuiltin("Container.SetViewMode(500)")

def pornohub_networksmenu():
        addLink("[B][COLOR white] NETWORKS [/COLOR][/B]",'','-')

        addDir("21 Sextury",'http://pornohub.su/porn/21sextury/',151,artfolder + 'videos.png')
        addDir("Babes Network",'http://pornohub.su/porn/babes-network/',151,artfolder + 'videos.png')
        addDir("Brazzers",'http://pornohub.su/porn/brazzers/',151,artfolder + 'videos.png')
        addDir("Burning Angel",'http://pornohub.su/porn/burningangel/',151,artfolder + 'videos.png')
        addDir("Cum Louder",'http://pornohub.su/porn/cumlouder/',151,artfolder + 'videos.png')
        addDir("DDF Network",'http://pornohub.su/porn/ddfnetwork/',151,artfolder + 'videos.png')
        addDir("Digital Playground",'http://pornohub.su/porn/digitalplayground/',151,artfolder + 'videos.png')
        addDir("Dogfart Network",'http://pornohub.su/porn/dogfartnetwork/',151,artfolder + 'videos.png')
        addDir("Evil Angel",'http://pornohub.su/porn/evil-angel/',151,artfolder + 'videos.png')
        addDir("Fake Hub",'http://pornohub.su/porn/fakehub/',151,artfolder + 'videos.png')
        addDir("Jacquie Et Michel TV",'http://pornohub.su/porn/jacquieetmicheltv/',151,artfolder + 'videos.png')
        addDir("Jules Jordan",'http://pornohub.su/porn/jules-jordan/',151,artfolder + 'videos.png')
        addDir("Killergram",'http://pornohub.su/porn/killergram/',151,artfolder + 'videos.png')
        addDir("Kink",'http://pornohub.su/porn/kink/',151,artfolder + 'videos.png')
        addDir("Mofos",'http://pornohub.su/porn/mofos/',151,artfolder + 'videos.png')
        addDir("Naughty America",'http://pornohub.su/porn/naughtyamerica/',151,artfolder + 'videos.png')
        addDir("Nubiles Network",'http://pornohub.su/porn/nubiles-network/',151,artfolder + 'videos.png')
        addDir("Perfect Gonzo",'http://pornohub.su/porn/perfectgonzo/',151,artfolder + 'videos.png')
        addDir("Porn",'http://pornohub.su/porn/',151,artfolder + 'videos.png')
        addDir("Puba",'http://pornohub.su/porn/puba/',151,artfolder + 'videos.png')
        addDir("Realitykings",'http://pornohub.su/porn/realitykings/',151,artfolder + 'videos.png')
        addDir("Spizoo",'http://pornohub.su/porn/spizoo/',151,artfolder + 'videos.png')
        addDir("Tainster",'http://pornohub.su/porn/tainster/',151,artfolder + 'videos.png')
        addDir("Team Skeet",'http://pornohub.su/porn/teamskeet/',151,artfolder + 'videos.png')
        addDir("Teen Mega World",'http://pornohub.su/porn/teenmegaworld/',151,artfolder + 'videos.png')
        addDir("Tushy",'http://pornohub.su/porn/tushy/',151,artfolder + 'videos.png')
        addDir("Twistys",'http://pornohub.su/porn/twistys/',151,artfolder + 'videos.png')
        addDir("Wankz",'http://pornohub.su/porn/wankz/',151,artfolder + 'videos.png')
        addDir("Wicked",'http://pornohub.su/porn/wicked/',151,artfolder + 'videos.png')


        xbmc.executebuiltin("Container.SetViewMode(50)")

def pornohub_menu():
        addLink("[B][COLOR white]PORNOHUB[/COLOR][/B]",'','-')

        addDir("At School",'http://pornohub.su/porn/brazzers/big-tits-at-school/',151,artfolder + 'videos.png')
        addDir("At Work",'http://pornohub.su/porn/brazzers/big-tits-at-work/',151,artfolder + 'videos.png')
        addDir("Baby Got Boobs",'http://pornohub.su/porn/brazzers/baby-got-boobs/',151,artfolder + 'videos.png')
        addDir("Big Butts Like It Big",'http://pornohub.su/porn/brazzers/big-butts-like-it-big/',151,artfolder + 'videos.png')
        addDir("Big Wet Butts",'http://pornohub.su/porn/brazzers/big-wet-butts/',151,artfolder + 'videos.png')
        addDir("Day With A Pornstar",'http://pornohub.su/porn/brazzers/daywithapornstar/',151,artfolder + 'videos.png')
        addDir("Dirty Masseur",'http://pornohub.su/porn/brazzers/dirty-masseur/',151,artfolder + 'videos.png')
        addDir("Doctor Adventures",'http://pornohub.su/porn/brazzers/doctor-adventures/',151,artfolder + 'videos.png')
        addDir("Exxtra",'http://pornohub.su/porn/brazzers/brazzers-exxtra/',151,artfolder + 'videos.png')
        addDir("Hot And Mean",'http://pornohub.su/porn/brazzers/hot-and-mean/',151,artfolder + 'videos.png')
        addDir("Milfs Like It Big",'http://pornohub.su/porn/brazzers/milfs-like-it-big/',151,artfolder + 'videos.png')
        addDir("Mofos HD 720",'http://pornohub.su/porn/mofos/',151,artfolder + 'videos.png')
        addDir("Mommy Got Boobs",'http://pornohub.su/porn/brazzers/mommy-got-boobs/',151,artfolder + 'videos.png')
        addDir("Moms In Control",'http://pornohub.su/porn/brazzers/moms-in-control/',151,artfolder + 'videos.png')
        addDir("Pornstars Like It Big",'http://pornohub.su/porn/brazzers/pornstars-like-it-big/',151,artfolder + 'videos.png')
        addDir("Premium Selection",'http://pornohub.su/porn/premium-selection/',151,artfolder + 'videos.png')
        addDir("Real Wife Stories",'http://pornohub.su/porn/brazzers/real-wife-stories/',151,artfolder + 'videos.png')
        addDir("Sports",'http://pornohub.su/porn/brazzers/big-tits-in-sports/',151,artfolder + 'videos.png')
        addDir("Teens Like It Big",'http://pornohub.su/porn/brazzers/teens-like-it-big/',151,artfolder + 'videos.png')
        addDir("Uniform",'http://pornohub.su/porn/brazzers/big-tits-at-uniform/',151,artfolder + 'videos.png')
        addDir("ZZSeries",'http://pornohub.su/porn/brazzers/zzseries/',151,artfolder + 'videos.png')

        xbmc.executebuiltin("Container.SetViewMode(50)")

        return

        url = "http://pornohub.su/porn/brazzers/baby-got-boobs/"
        codigo_fonte = abrir_url(url)
        
        match = re.compile('<li class="menu-item-0"><a href="(.+?)"').findall(codigo_fonte)
        match2 = re.compile('<a href=".+">(.+?)</a>').findall(codigo_fonte)

        a = []
        for x in range(0, len(match)):
                temp = [match[x],match2[x]]; 
                a.append(temp);
        total=len(a)
        for url,titulo in a:
                addDir(titulo,url,151,artfolder + 'videos.png')




        #addDir(traducao(2022),'http://brazzershd.net/',203,artfolder + 'search.png')
        #addDir(traducao(2023),'-',207,artfolder + 'cat.png')
        xbmc.executebuiltin("Container.SetViewMode(50)")
        
def archives():
        addLink("[B][COLOR white] ARCHIVES [/COLOR][/B]",'','-')

        addDir("2016",'http://pornohub.su/2016/',151,artfolder + 'videos.png')
        addDir("2015",'http://pornohub.su/2015/',151,artfolder + 'videos.png')
        addDir("2014",'http://pornohub.su/2014/',151,artfolder + 'videos.png')
        addDir("2013",'http://pornohub.su/2013/',151,artfolder + 'videos.png')
        addDir("2012",'http://pornohub.su/2012/',151,artfolder + 'videos.png')
        addDir("2011",'http://pornohub.su/2011/',151,artfolder + 'videos.png')
        addDir("2010",'http://pornohub.su/2010/',151,artfolder + 'videos.png')
        addDir("2009",'http://pornohub.su/2009/',151,artfolder + 'videos.png')
        addDir("2008",'http://pornohub.su/2008/',151,artfolder + 'videos.png')
        addDir("2007",'http://pornohub.su/2007/',151,artfolder + 'videos.png')

        xbmc.executebuiltin("Container.SetViewMode(50)")


def mode(mode,name,url,iconimage):
        if mode==101: pornohub_mainmenu()
        elif mode==140: pornohub_networksmenu()
        elif mode==150: pornohub_menu()
        elif mode==151: listar_videos(url)
        elif mode==152: encontrar_fontes(name,url,iconimage)
        elif mode==153: listar_videos_pornstar(url)
        elif mode==180: pesquisa()
        elif mode==190: archives()
        elif mode==205: download(name,url)
        elif mode==206: selfAddon.openSettings()
        elif mode==160: cat()
        elif mode==170: pornstars()
        elif mode==171: pornstars_next(url)
        
        
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
        
def pornstars():
        codigo_fonte = abrir_url('http://pornohub.su/pornstars/')
        match = re.compile('<div class="td-module-thumb">(.+?)</div>').findall(codigo_fonte)
        for pstar in match:
                match2 = re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)"><img width="356" height="364" itemprop="image" class="entry-thumb" src="(.+?)"',flags=re.IGNORECASE).findall(pstar)
                for url, titulo, img in match2:
                        parametro_pesquisa=titulo.replace(" ","+")
                        url = 'http://pornohub.su/?s=' + str(parametro_pesquisa)
                        addDir(titulo,url,151,img)
        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                addDir(traducao(2050),url,171,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass

        xbmc.executebuiltin("Container.SetViewMode(500)")

def pornstars_next(url):
        print 'pornstars_next: '+url
        codigo_fonte = abrir_url(url)
        match = re.compile('<div class="td-module-thumb">(.+?)</div>').findall(codigo_fonte)
        for pstar in match:
                match2 = re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)"><img width="356" height="364" itemprop="image" class="entry-thumb" src="(.+?)"',flags=re.IGNORECASE).findall(pstar)
                for url, titulo, img in match2:
                        parametro_pesquisa=titulo.replace(" ","+")
                        url = 'http://pornohub.su/?s=' + str(parametro_pesquisa)
                        addDir(titulo,url,151,img)
        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                addDir(traducao(2050),url,171,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass

        xbmc.executebuiltin("Container.SetViewMode(500)")
        
def listar_videos_pornstar(url):
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")
        
        codigo_fonte_videos = re.compile('<div class="td-header-rec-wrap">(.*?)<div class="td-load-more-wrap">',flags=0).findall(codigo_fonte)

        try:
                page = int(re.compile('<span class="current">(.+?)</span>').findall(codigo_fonte)[0])
        except: page = 1

        a = []
        for m in codigo_fonte_videos:
                match = re.compile('<div class="td-module-thumb"><a href="(http.+?)" rel="bookmark" title="(.+?)"><img width="\d+" height="\d+" itemprop="image" class="(.+?)" src="(.+?)" alt=').findall(m)
                for x in range(0, len(match)):
                        temp = [match[x][0],match[x][1],match[x][3]]; 
                        if page > 1:
                                if x > 4: a.append(temp)
                        else: a.append(temp)
        total=len(a)
        #print 'rui test'
        #print total
        #print codigo_fonte_videos
        for url,titulo,img in a:
                if img[:2] == '//': img = 'http:' + img
                addDir(titulo,url,152,img,False,total,True)
        
        try:
                next_page = re.compile('<link rel="canonical" href="(.+?)"/>').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][0]
                print 'Next: '+url
                addDir(traducao(2050),url,151,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass
        
        xbmc.executebuiltin("Container.SetViewMode(500)")
        
def listar_videos(url):
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")
        
        codigo_fonte_videos = re.compile('<div class="td-header-rec-wrap">(.*?)<div class="td-footer-wrapper">',flags=0).findall(codigo_fonte)

        try:
                page = int(re.compile('<span class="current">(.+?)</span>').findall(codigo_fonte)[0])
        except: page = 1

        a = []
        for m in codigo_fonte_videos:
                match = re.compile('<div class="td-module-thumb"><a href="(http.+?)" rel="bookmark" title="(.+?)"><img width="\d+" height="\d+" itemprop="image" class="(.+?)" src="(.+?)" alt=').findall(m)
                for x in range(0, len(match)):
                        temp = [match[x][0],match[x][1],match[x][3]]; 
                        if page > 1:
                                if x > 4: a.append(temp)
                        else: a.append(temp)
        total=len(a)
        #print 'rui test'
        #print total
        #print codigo_fonte_videos
        for url,titulo,img in a:
                if img[:2] == '//': img = 'http:' + img
                addDir(titulo,url,152,img,False,total,True)
        
        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                addDir(traducao(2050),url,151,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass
        
        xbmc.executebuiltin("Container.SetViewMode(500)")

        
def encontrar_fontes(name,url,iconimage):
        #mensagemprogresso.create('Adults TV', traducao(2008),traducao(2009))
        #mensagemprogresso.update(0)
        html = abrir_url(url)
        try: 
                video_url = re.compile('<source type="video/mp4" src="(.+?mp4).*"').findall(html)[0]
        except: return

        #url_video = urllib.quote(video_url)
        #url_video = url_video.replace("%3A",":")
        url_video = video_url
        
        if url_video: play(name,url_video,iconimage)
        
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
                url = 'http://pornohub.su/?s=' + str(parametro_pesquisa)
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
