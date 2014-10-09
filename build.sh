while ,watch -q -r .
do
    rst2html.py \
        --smart-quotes=yes \
        --stylesheet-path=./static/pygments.css,./static/slides2.css \
        --link-stylesheet \
        --syntax-highlight=short \
        english_number.rst > english_number.html

    # BROWSER=$(xdotool search --onlyvisible --class chromium|head -1)
    # MYWINDOW=$(xdotool getactivewindow)

    # #
    # # bring up the browser
    # xdotool windowactivate ${BROWSER}
    # # send the page-reload keys (C-R) or (S-C-R)
    # xdotool key --clearmodifiers ctrl+F5
    # #
    # # sometimes the focus doesn't work, so follow up with activate
    # xdotool windowfocus --sync ${MYWINDOW}
    # xdotool windowactivate --sync ${MYWINDOW}

    py.test -qx
done
