main () {
    # The function which runs the entire script
    killall -q tor chrome dropbox iceweasel skype icedove thunderbird firefox chromium xchat transmission deluge pidgin pidgin.orig
    # bleachbit -c adobe_reader.cache chromium.cache chromium.current_session chromium.history elinks.history emesene.cache epiphany.cache firefox.url_history flash.cache flash.cookies google_chrome.cache google_chrome.history  links2.history opera.cache opera.search_history opera.url_history &> /dev/null
}

# Calling the main function.
main
