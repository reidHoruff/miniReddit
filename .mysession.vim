let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +22 ~/dev/mini_reddit/README.md
badd +1 ~/dev/mini_reddit/minireddit/www/models.py
badd +1 ~/dev/mini_reddit/minireddit/www/migrations/__init__.py
badd +81 ~/dev/mini_reddit/minireddit/minireddit/settings.py
badd +1 ~/dev/mini_reddit/minireddit/static/test.js
badd +16 ~/dev/mini_reddit/minireddit/templates/base.html
badd +1 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +5 ~/dev/mini_reddit/minireddit/templates/home.html
badd +12 ~/dev/mini_reddit/minireddit/www/views.py
badd +12 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +20 ~/dev/mini_reddit/minireddit/templates/register.html
badd +1 ~/dev/mini_reddit/minireddit/static/css/register.html
badd +76 ~/.vimrc
badd +8 ~/dev/mini_reddit/minireddit/www/async.py
badd +106 ~/dev/mini_reddit/minireddit/www/forms.py
argglobal
silent! argdel *
edit ~/dev/mini_reddit/minireddit/www/views.py
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
let s:l = 13 - ((12 * winheight(0) + 26) / 52)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
13
normal! 052|
wincmd w
argglobal
edit ~/dev/mini_reddit/minireddit/templates/register.html
let s:l = 20 - ((19 * winheight(0) + 26) / 52)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
20
normal! 014|
wincmd w
2wincmd w
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
