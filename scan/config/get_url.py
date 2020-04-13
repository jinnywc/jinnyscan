def get_url(url):
    if "://" in url:
        tmp_url = url
        sign = tmp_url.split("//", 1)[1]
        if "/" in sign:
            if sign.split("/", 1)[1]:
                sign = sign.split("/", 1)[1]
                target_url = tmp_url.split(sign, 1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    else:
        tmp_url = "http://" + url
        sign = tmp_url.split("//", 1)[1]
        if "/" in sign:
            if sign.split("/", 1)[1]:
                sign = sign.split("/", 1)[1]
                target_url = tmp_url.split(sign, 1)[0]
            else:
                target_url = tmp_url
        else:
            target_url = tmp_url + "/"
    return target_url