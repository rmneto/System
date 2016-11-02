#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 2014 - Anonymous

import urllib,urllib2,re,HTMLParser,os,sys,time
import hqqresolver

def abrir_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def abrir_url_ref(url,ref_url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        req.add_header('Referer', ref_url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def listar_videos(url):
        codigo_fonte = abrir_url(url)
        
        match = re.compile('<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(http.+?)" rel="bookmark" title="(.+?)"').findall(codigo_fonte)
        match3 = re.compile('<img.+src="(.+?).jpg"').findall(codigo_fonte)

        a = []
        for x in range(0, len(match)):
                temp = [match[x][0],match[x][1],match3[x]]; 
                if x > 14: a.append(temp);
        total=len(a)
        for url,titulo,img in a:
                titulo = titulo.replace("&#8211;","-")
                titulo = titulo.replace("&#8217;","'")
                if img[:2] == '//': img = 'http:' + img
                #addDir(titulo,url,152,img+'.jpg',False,total,True)
        
        try:
                page = re.compile('<link rel="next" href="(.+?)"').findall(codigo_fonte)[0]
                if page[:2] == '//': page = 'http:' + page
                #addDir(traducao(2050),page,201,artfolder + 'next.png')
        except: pass

def cat():
        codigo_fonte = abrir_url('http://pornohub.su/')
        match = re.compile('<li class="menu-item menu-item-type-taxonomy menu-item-object-category td-menu-item td-normal-menu menu-item-110">(.+?)</ul></li>',flags=0).findall(codigo_fonte)
        match2 = re.compile('<a href="(.+?)" rel="bookmark" >(.+?)</a>').findall(match[0])
        #print match
        for url,titulo in match2:
                print url + ' ' + titulo
                
        return

def pornstars():
        codigo_fonte = abrir_url('http://pornohub.su/pornstars/')
        match = re.compile('<div class="td-module-thumb">(.+?)</div>').findall(codigo_fonte)
        for pstar in match:
                match2 = re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)"><img width="356" height="364" itemprop="image" class="entry-thumb" src="(.+?)"',flags=re.IGNORECASE).findall(pstar)
                for url, titulo, img in match2:
                        parametro_pesquisa=urllib.quote(titulo)
                        url = 'http://pornohub.su/?s=' + str(parametro_pesquisa)
                        print url
        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass
                        
def listar_videos():
        #codigo_fonte = abrir_url('http://pornohub.su/porn/premium-selection/page/2/')
        #codigo_fonte = abrir_url('http://pornohub.su/porn/premium-selection/')
        codigo_fonte = abrir_url('http://pornohub.su/porn/brazzers/baby-got-boobs/page/2/')
        #codigo_fonte = abrir_url('http://pornohub.su/?s=Stella+Cox')

        codigo_fonte = codigo_fonte.replace("\n","")
        
        codigo_fonte_videos = re.compile('<div class="td-header-rec-wrap">(.*?)<div class="td-footer-wrapper">',flags=0).findall(codigo_fonte)

        page = int(re.compile('<span class="current">(.+?)</span>').findall(codigo_fonte)[0])

        a = []
        for m in codigo_fonte_videos:
                match = re.compile('<div class="td-module-thumb"><a href="(http.+?)" rel="bookmark" title="(.+?)"><img width="\d+" height="\d+" itemprop="image" class="(.+?)" src="(.+?)" alt=').findall(m)
                for x in range(0, len(match)):
                        #print match[x][0]
                        temp = [match[x][0],match[x][1],match[x][2]];
                        if len(match[x][0]) > 5: a.append(temp)
        total=len(a)
        for url,titulo,img in a:
                if img[:2] == '//': img = 'http:' + img
                #addDir(titulo,url,152,img,False,total,True)
                print titulo

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
                #addDir(titulo,url,152,img,False,total,True)
                print titulo

        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                #print next_page
                url = next_page[len(next_page)-1][1]
                #print 'Next: '+url
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass

def listar_videos_bdh(url):
        url = "http://brazzershd.net/tag/big-tits/"
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")
        
        codigo_fonte_videos = re.compile('<a class="clip-link"(.+?)</a>',flags=0).findall(codigo_fonte)

        try:
                page = int(re.compile('<span class="current">(.+?)</span>').findall(codigo_fonte)[0])
        except: page = 1

        a = []
        i=0

        t = url.find("/tag/")
        if t>0: i=100
        print 'rui test'
        print url
        print t

        for m in codigo_fonte_videos:
                match = re.compile('title="(.+?)" href="(.+?)">.*<img src="(.+?)"').findall(m)
                for x in range(0, len(match)):
                        temp = [match[x][1],match[x][0],match[x][2]]
                        #print i
                        a.append(temp)
                i=i+1
        total=len(a)
        #print 'rui test'
        #print total
        #print codigo_fonte_videos
        for url,titulo,img in a:
                if img[:2] == '//': img = 'http:' + img
                print titulo
                #addDir(titulo,url,152,img,False,total,True)
        
        try:
                next_page = re.compile('<span class="current">(.+?)</span><a href="(http.+?)" class="page" title="(.+?)"').findall(codigo_fonte)
                print next_page
                url = next_page[len(next_page)-1][1]
                print 'Next: '+url
                #addDir(traducao(2050),url,151,artfolder + 'next.png')
                #addDir("total "+len(a),url,151,artfolder + 'next.png')
        except: pass
        
        #xbmc.executebuiltin("Container.SetViewMode(500)")

def encontrar_fontes(url):
        codigo_fonte = abrir_url(url)
        codigo_fonte = codigo_fonte.replace("\n","")

        iframe_url = re.compile('<iframe src="(.+?)" scrolling="no"').findall(codigo_fonte)
        print iframe_url
        if len(iframe_url)==0 or iframe_url[0].find(".mp4")>0:
                script_url = re.compile('<div class="screen fluid-width-video-wrapper">.*<script src="(.+?)">.*<script src="(.+?)">').findall(codigo_fonte)[0]
                hash_url = script_url[0]
                iframe_url = script_url[1]
                print iframe_url
                codigo_fonte = abrir_url_ref(hash_url,url)
                codigo_fonte = urllib.unquote(codigo_fonte)
                vid = re.compile("var vid = '(.+?)'").findall(codigo_fonte)[0]
                hash_from = re.compile("var hash_from = '(.+?)'").findall(codigo_fonte)[0]
                print vid
                print hash_from
                

                codigo_fonte = abrir_url_ref(iframe_url,url)
                codigo_fonte = codigo_fonte.replace("\n","")
                #print codigo_fonte
                iframe_url = re.compile('<iframe src="(.+?)"').findall(codigo_fonte)[0]
                iframe_url = iframe_url.replace("'+vid+'",vid)
                iframe_url = iframe_url.replace("'+hash_from+'",hash_from)
                iframe_url = iframe_url.replace("&amp;","&")

                print iframe_url
                if re.search('hqq.tv',iframe_url): url_video = hqq_resolver(iframe_url)
                print 'hqq_resolver:'
                print url_video
        else:
                codigo_fonte = abrir_url(iframe_url[0])
                codigo_fonte = codigo_fonte.replace("\n","")
                sources = re.compile("{file:'(.+?)',label:'(.+?)',type: '(.+?)'}").findall(codigo_fonte)
                print sources[len(sources)-1][0]
                video_url = sources[len(sources)-1][0]
                
        print iframe_url
        print video_url


        url_video = urllib.unquote(video_url)

def encontrar_fontes2(url):
        #mensagemprogresso.create('Adults TV', traducao(2008),traducao(2009))
        #mensagemprogresso.update(0)
        html = abrir_url(url)
        video_url = re.compile('<source type="video/mp4" src="(.+?mp4).*"').findall(html)[0]

        url_video = urllib.quote(video_url)
        print url_video
                
url = 'http://brazzershd.net/category/brazzers-hd/?orderby=date'
#listar_videos_bdh(url)
#listar_categories()


url = 'http://brazzershd.net/brazzers-hd/a-dick-before-dropout-2/'
url = 'http://brazzershd.net/brazzers-hd/hot-cop-mean-cop-2/'
url = "http://brazzershd.net/brazzers-hd/yoga-lesson-4/"
url = "http://pornohub.su/burningangel-lily-lane-double-penetration-04-02-2016/"
encontrar_fontes2(url)
url = "http://hqq.tv/player/embed_player.php?vid=S28KYARU5N4Y&autoplay=none&hash_from=5fce1e35839e0c280612fa8ef19b6c92"
#hqqvidresolver = hqqresolver.hqqResolver()
#r = hqqvidresolver.resolve("S28KYARU5N4Y")
#print r
