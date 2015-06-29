let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +40 ~/dev/mini_reddit/minireddit/templates/with_side.html
badd +3 ~/dev/mini_reddit/minireddit/static/css/with_side.css
badd +28 ~/dev/mini_reddit/minireddit/templates/base.html
badd +53 ~/dev/mini_reddit/minireddit/www/views.py
badd +12 ~/dev/mini_reddit/minireddit/templates/submit.html
badd +114 ~/dev/mini_reddit/minireddit/www/forms.py
badd +142 ~/dev/mini_reddit/minireddit/www/async.py
badd +13 ~/dev/mini_reddit/minireddit/templates/post.html
badd +34 ~/dev/mini_reddit/minireddit/static/css/post.css
badd +23 ~/dev/mini_reddit/minireddit/templates/home.html
badd +62 ~/dev/mini_reddit/minireddit/www/models.py
badd +26 ~/dev/mini_reddit/minireddit/minireddit/urls.py
badd +53 ~/dev/mini_reddit/minireddit/static/css/base.css
badd +23 ~/dev/mini_reddit/minireddit/templates/createsub.html
badd +13 ~/dev/mini_reddit/minireddit/static/css/home.css
badd +6 ~/dev/mini_reddit/minireddit/templates/replybox.html
badd +138 ~/dev/mini_reddit/minireddit/sniper/snipers.py
badd +32 ~/dev/mini_reddit/minireddit/static/js/sniper.js
badd +21 ~/dev/mini_reddit/minireddit/templates/recur_comment_view.html
badd +14 ~/dev/mini_reddit/minireddit/templates/profile.html
badd +1 ~/dev/mini_reddit/minireddit/templates/register.html
badd +4 ~/dev/mini_reddit/minireddit/static/css/profile.css
badd +65 ~/dev/mini_reddit/minireddit/minireddit/settings.py
badd +63 ~/dev/mini_reddit/minireddit/www/management/commands/rpull.py
badd +81 ~/dev/mini_reddit/minireddit/sniper/sniper.py
badd +23 ~/dev/mini_reddit/minireddit/sniper/decorators.py
badd +24 ~/dev/mini_reddit/minireddit/templates/login.html
badd +186 ~/.vimrc
badd +174 ~/dev/mini_reddit/minireddit/sniper/static/sniper/sniper.js
badd +7 ~/dev/mini_reddit/requirements.pip
badd +1 ~/dev/mini_reddit/minireddit/pulled
argglobal
silent! argdel *
edit ~/dev/mini_reddit/minireddit/pulled
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
let s:l = 1 - ((0 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
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
