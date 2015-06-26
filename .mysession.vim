let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 ~/dev/mini_reddit/README.md
badd +1 ~/dev/mini_reddit/minireddit/www/models.py
badd +1 ~/dev/mini_reddit/minireddit/www/migrations/__init__.py
badd +81 ~/dev/mini_reddit/minireddit/minireddit/settings.py
badd +1 ~/dev/mini_reddit/minireddit/static/test.js
badd +16 ~/dev/mini_reddit/minireddit/templates/base.html
badd +1 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +5 ~/dev/mini_reddit/minireddit/templates/home.html
badd +1 ~/dev/mini_reddit/minireddit/www/views.py
badd +12 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +1 ~/dev/mini_reddit/minireddit/templates/register.html
badd +1 ~/dev/mini_reddit/minireddit/static/css/register.html
badd +85 ~/.vimrc
badd +8 ~/dev/mini_reddit/minireddit/www/async.py
badd +106 ~/dev/mini_reddit/minireddit/www/forms.py
badd +20 ~/dev/miniReddit/minireddit/templates/home.html
badd +14 ~/dev/miniReddit/minireddit/templates/login.html
badd +36 ~/dev/miniReddit/minireddit/www/views.py
badd +1 ~/dev/miniReddit/minireddit/static/css/home.css
badd +25 ~/dev/miniReddit/minireddit/templates/base.html
badd +1 ~/dev/miniReddit/minireddit/static/login.css
badd +136 ~/dev/miniReddit/minireddit/www/forms.py
badd +85 ~/dev/miniReddit/minireddit/www/async.py
badd +16 ~/dev/miniReddit/minireddit/templates/submit.html
badd +20 ~/dev/miniReddit/minireddit/minireddit/urls.py
badd +1 ~/dev/miniReddit/minireddit/templates/createsub.html
badd +1 ~/dev/miniReddit/minireddit/static/css/createsub.css
badd +1 ~/dev/miniReddit/minireddit/static/css/submit.css
badd +17 ~/dev/miniReddit/minireddit/static/css/base.css
badd +17 ~/dev/miniReddit/minireddit/www/models.py
badd +6 ~/dev/miniReddit/minireddit/www/admin.py
badd +5 ~/dev/miniReddit/minireddit/sniper/sniper.py
badd +1 ~/dev/miniReddit/minireddit/sniper/decorators.py
badd +13 ~/dev/miniReddit/minireddit/templates/with_side.html
badd +39 ~/dev/miniReddit/minireddit/templates/post.html
badd +1 ~/dev/miniReddit/minireddit/static/css/with_side.css
badd +39 ~/dev/miniReddit/minireddit/static/css/post.css
badd +1 ~/dev/miniReddit/minireddit/templates/reply.html
argglobal
silent! argdel *
edit ~/dev/miniReddit/minireddit/www/async.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
let s:l = 133 - ((22 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
133
normal! 017|
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
