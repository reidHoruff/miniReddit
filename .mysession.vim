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
badd +27 ~/dev/mini_reddit/minireddit/templates/base.html
badd +35 ~/dev/mini_reddit/minireddit/www/views.py
badd +15 ~/dev/mini_reddit/minireddit/templates/submit.html
badd +22 ~/dev/mini_reddit/minireddit/www/forms.py
badd +79 ~/dev/mini_reddit/minireddit/www/async.py
badd +28 ~/dev/mini_reddit/minireddit/templates/post.html
badd +15 ~/dev/mini_reddit/minireddit/static/css/post.css
badd +21 ~/dev/mini_reddit/minireddit/templates/home.html
badd +24 ~/dev/mini_reddit/minireddit/www/models.py
badd +15 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +11 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +23 ~/dev/mini_reddit/minireddit/templates/createsub.html
argglobal
silent! argdel *
edit ~/dev/mini_reddit/minireddit/www/async.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
let s:l = 84 - ((30 * winheight(0) + 25) / 50)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
84
normal! 014|
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
