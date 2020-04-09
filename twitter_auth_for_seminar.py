#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session





def authorize():
    CK = "2DNgZYGaEn3tTCGKxGH9fQSig"
    CS = "abVyHs1ah7lPh3PfdA34BP9D2k5pt4M7sBJ4lPFjgKHH9AHNoH"
    AT = "804336950589190145-OkVn4m41v5zGmAYZjJw2eIjdXmKGE6m"
    ATS = "jJsIIJcdpm9kuMoat1UnPsj6OXXc2a738nYcjxAk9cph5"
    auth_object = OAuth1Session(CK, CS, AT, ATS)

    return auth_object


