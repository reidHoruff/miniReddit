let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +51 ~/dev/mini_reddit/minireddit/templates/with_side.html
badd +15 ~/dev/mini_reddit/minireddit/static/css/with_side.css
badd +13 ~/dev/mini_reddit/minireddit/templates/base.html
badd +41 ~/dev/mini_reddit/minireddit/www/views.py
badd +12 ~/dev/mini_reddit/minireddit/templates/submit.html
badd +114 ~/dev/mini_reddit/minireddit/www/forms.py
badd +248 ~/dev/mini_reddit/minireddit/www/async.py
badd +7 ~/dev/mini_reddit/minireddit/templates/post.html
badd +58 ~/dev/mini_reddit/minireddit/static/css/post.css
badd +29 ~/dev/mini_reddit/minireddit/templates/home.html
badd +33 ~/dev/mini_reddit/minireddit/www/models.py
badd +7 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +17 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +23 ~/dev/mini_reddit/minireddit/templates/createsub.html
badd +35 ~/dev/mini_reddit/minireddit/static/css/home.css
badd +3 ~/dev/mini_reddit/minireddit/templates/replybox.html
badd +138 ~/dev/mini_reddit/minireddit/sniper/snipers.py
badd +159 ~/dev/mini_reddit/minireddit/static/js/sniper.js
badd +29 ~/dev/mini_reddit/minireddit/templates/recur_comment_view.html
badd +14 ~/dev/mini_reddit/minireddit/templates/profile.html
badd +1 ~/dev/mini_reddit/minireddit/templates/register.html
badd +4 ~/dev/mini_reddit/minireddit/static/css/profile.css
badd +43 ~/dev/mini_reddit/minireddit/minireddit/settings.py
badd +27 ~/dev/mini_reddit/minireddit/www/management/commands/rpull.py
badd +81 ~/dev/mini_reddit/minireddit/sniper/sniper.py
badd +23 ~/dev/mini_reddit/minireddit/sniper/decorators.py
badd +24 ~/dev/mini_reddit/minireddit/templates/login.html
badd +186 ~/.vimrc
badd +174 ~/dev/mini_reddit/minireddit/sniper/static/sniper/sniper.js
badd +4 ~/dev/mini_reddit/requirements.pip
badd +1 ~/dev/mini_reddit/minireddit/pulled
badd +9 ~/dev/mini_reddit/minireddit/www/admin.py
badd +21 ~/dev/mini_reddit/WordSoFar.txt
badd +10 ~/dev/mini_reddit/Changes.txt
badd +5 ~/dev/mini_reddit/Plan.txt
argglobal
silent! argdel *
edit ~/dev/mini_reddit/Plan.txt
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
wincmd =
argglobal
let s:l = 9 - ((8 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
9
normal! 093|
wincmd w
argglobal
edit ~/dev/mini_reddit/minireddit/www/views.py
let s:l = 59 - ((45 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
59
normal! 013|
wincmd w
wincmd =
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOc
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
