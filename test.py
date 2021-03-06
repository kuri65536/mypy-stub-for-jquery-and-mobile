#
# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Text

import jquery

# __pragma__("skip")
from jQuery import jqXHR

if False:
    Text
    jqXHR
# __pragma__("noskip")


def on_click(ev):  # {{{1
    # type: (jquery.Event) -> bool
    jquery.ajax({"url": "http://localhost:8000/test-ajax-src.html",
                 "timeout": 1000}) \
          .then(ajax_load, ajax_fail)
    return False


def ajax_load(_dat, stat, xhr):  # {{{1
    # type: (Text, Text, jqXHR) -> bool
    jquery.debg("ajax")
    dom = jquery.parseHTML(_dat)
    seq = jquery.jq(dom).filter("div")  # selector and find() not worked.

    sel = jquery.jq("#sel")
    for _div in seq:
        jquery.debg("loop")
        div = jquery.jq(_div)
        sel.append('<option value="{}">{}</option>'.format(
                   div.attr("id"), div.text()))
    return True


def ajax_fail():  # {{{1
    # type: () -> None
    pass


def main(ev):  # {{{1
    # type: (jquery.Event) -> bool
    jquery.jq("#sample").off("click").on("click", on_click)

    # wrong code
    btn = jquery.jq("#sample")
    div = jquery.jq(btn, "div.abc")
    div
    return False


jquery.on_load(main)

if __name__ == "__main__":  # {{{1
    ev = jquery.dummy_event()
    main(ev)
# vi: ft=python:et:ts=4:fdm=marker:nowrap
