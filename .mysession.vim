let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +47 ~/dev/mini_reddit/minireddit/templates/with_side.html
badd +12 ~/dev/mini_reddit/minireddit/static/css/with_side.css
badd +13 ~/dev/mini_reddit/minireddit/templates/base.html
badd +67 ~/dev/mini_reddit/minireddit/www/views.py
badd +15 ~/dev/mini_reddit/minireddit/templates/submit.html
badd +131 ~/dev/mini_reddit/minireddit/www/forms.py
badd +85 ~/dev/mini_reddit/minireddit/www/async.py
badd +19 ~/dev/mini_reddit/minireddit/templates/post.html
badd +35 ~/dev/mini_reddit/minireddit/static/css/post.css
badd +21 ~/dev/mini_reddit/minireddit/templates/home.html
badd +29 ~/dev/mini_reddit/minireddit/www/models.py
badd +22 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +70 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +23 ~/dev/mini_reddit/minireddit/templates/createsub.html
badd +13 ~/dev/mini_reddit/minireddit/static/css/home.css
badd +6 ~/dev/mini_reddit/minireddit/templates/replybox.html
badd +105 ~/dev/mini_reddit/minireddit/sniper/snipers.py
badd +36 ~/dev/mini_reddit/minireddit/static/js/sniper.js
badd +4 ~/dev/mini_reddit/minireddit/templates/recur_comment_view.html
badd +0 ~/dev/mini_reddit/minireddit/templates/profile.html
badd +1 ~/dev/mini_reddit/minireddit/templates/register.html
badd +4 ~/dev/mini_reddit/minireddit/static/css/profile.css
argglobal
silent! argdel *
edit ~/dev/mini_reddit/minireddit/templates/home.html
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
3wincmd h
wincmd w
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
wincmd =
argglobal
let s:l = 19 - ((18 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 0
wincmd w
argglobal
edit ~/dev/mini_reddit/minireddit/templates/profile.html
let s:l = 14 - ((13 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
14
normal! 073|
wincmd w
argglobal
edit ~/dev/mini_reddit/minireddit/templates/recur_comment_view.html
let s:l = 6 - ((5 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 078|
wincmd w
argglobal
edit ~/dev/mini_reddit/minireddit/www/models.py
let s:l = 19 - ((18 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 033|
wincmd w
4wincmd w
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
