# -*- coding: utf-8 -*-
from apiAutomation.utils import Encrypt

queryItcs = {
    "itc" : '234'
}
sendSmsData = [
    {
        "name": "8021300100 up to limit,get sms failed",
        "phoneNumber": "8021300100",
        "itc": "234",
        "verifyType": 0,
        "errcode": 400003
    },
    {
        "name": "802130010,this phonenumber's format is error",
        "phoneNumber": "802130010",
        "itc": "234",
        "verifyType": 0,
        "errcode": 400
    },
    {
        "name": "phonenumber is null",
        "itc": "234",
        "verifyType": 0,
        "errcode": 400
    }
]
loginOrRegisterData = [
    {
        "name": "login by phoneNumber successfully",
        "phoneNumber": "8021300104",
        "itc": "234",
        "verificationCode": "",
        "verifyType": 0,
        "authType": 3
    }, {
        "name": "login by google successfully",
        "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk2OTcxODA4Nzk2ODI5YT\
        k3MmU3OWE5ZDFhOWZmZjExY2Q2MWIxZTMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiO\
        iJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI2NzM2MTU0MTQ\
        0OTYtMTQwbjEzYWhvYTR1M2o4OTVicDBla2xvcmwwaDZtZm0uYXBwcy5nb29nb\
        GV1c2VyY29udGVudC5jb20iLCJhdWQiOiI2NzM2MTU0MTQ0OTYtNzlobDEwZDN\
        1cWdkMTh1bnBpOGVmMTlkNDlyYXA3bXEuYXBwcy5nb29nbGV1c2VyY29udGVud\
        C5jb20iLCJzdWIiOiIxMDY0Mzk0NzM5MzM5OTg1MTcxOTYiLCJoZCI6ImlsbGl\
        ub2lzLmVkdSIsImVtYWlsIjoienhpM0BpbGxpbm9pcy5lZHUiLCJlbWFpbF92Z\
        XJpZmllZCI6dHJ1ZSwibmFtZSI6IlpoZW5nbGkgWGkiLCJwaWN0dXJlIjoiaHR\
        0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4Wi1wSHBNa\
        jNsbU9kZFhqUFg1XzhndHVMNlQzR2tINlFTQ0UzVzA9czk2LWMiLCJnaXZlbl9\
        uYW1lIjoiWmhlbmdsaSIsImZhbWlseV9uYW1lIjoiWGkiLCJsb2NhbGUiOiJlb\
        iIsImlhdCI6MTY4MTg3MDM3NywiZXhwIjoxNjgxODczOTc3fQ.k206nIkT2K4o\
        cLjeSdIaoQm21HB1mab06XcjAkfWhf6RThtrFVLtPt29XJtLj0i2w6XE3H6edj\
        tELAk122qUvEX_c-URxUrCN6e0yZ3uXxJnuoYNvTNWLwznjtK1_0_zQ9vK8oEZ\
        h13hqPUkFe9BSAHOmL4QqI9eRaUDm0bg3NXpObntrPxB5Vo105juGh3Cm_A6HS\
        -C_STzU_xUGC4qdwnBQDaxkVFEVi_CwtXokHx95RaQTbPcsmKrPWLhiOTXxSwX\
        wttaPE_XpfNNwJJlwypeyBFSLvc_DvLDuxdlL3aS47IRfUjZHjZxingSZI2mgk\
        krgr3Kr1jgFoV26z1Suw",
        "authType": 1
    }, {
        "name": "register by phone from inviter successfully",
        "phoneNumber": "8021300104",
        "itc": "234",
        "verificationCode": "",
        "verifyType": 0,
        "authType": 3,
        "inviteSeekId": Encrypt().aes_encrypt("65126515")
    }, {
        "name": "login by google from inviter successfully",
        "authorizationCode": "8021300102",
        "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk2OTcxODA4Nzk2ODI5YT\
        k3MmU3OWE5ZDFhOWZmZjExY2Q2MWIxZTMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiO\
        iJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI2NzM2MTU0MTQ\
        0OTYtMTQwbjEzYWhvYTR1M2o4OTVicDBla2xvcmwwaDZtZm0uYXBwcy5nb29nb\
        GV1c2VyY29udGVudC5jb20iLCJhdWQiOiI2NzM2MTU0MTQ0OTYtNzlobDEwZDN\
        1cWdkMTh1bnBpOGVmMTlkNDlyYXA3bXEuYXBwcy5nb29nbGV1c2VyY29udGVud\
        C5jb20iLCJzdWIiOiIxMDY0Mzk0NzM5MzM5OTg1MTcxOTYiLCJoZCI6ImlsbGl\
        ub2lzLmVkdSIsImVtYWlsIjoienhpM0BpbGxpbm9pcy5lZHUiLCJlbWFpbF92Z\
        XJpZmllZCI6dHJ1ZSwibmFtZSI6IlpoZW5nbGkgWGkiLCJwaWN0dXJlIjoiaHR\
        0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4Wi1wSHBNa\
        jNsbU9kZFhqUFg1XzhndHVMNlQzR2tINlFTQ0UzVzA9czk2LWMiLCJnaXZlbl9\
        uYW1lIjoiWmhlbmdsaSIsImZhbWlseV9uYW1lIjoiWGkiLCJsb2NhbGUiOiJlb\
        iIsImlhdCI6MTY4MTg3MDM3NywiZXhwIjoxNjgxODczOTc3fQ.k206nIkT2K4o\
        cLjeSdIaoQm21HB1mab06XcjAkfWhf6RThtrFVLtPt29XJtLj0i2w6XE3H6edj\
        tELAk122qUvEX_c-URxUrCN6e0yZ3uXxJnuoYNvTNWLwznjtK1_0_zQ9vK8oEZ\
        h13hqPUkFe9BSAHOmL4QqI9eRaUDm0bg3NXpObntrPxB5Vo105juGh3Cm_A6HS\
        -C_STzU_xUGC4qdwnBQDaxkVFEVi_CwtXokHx95RaQTbPcsmKrPWLhiOTXxSwX\
        wttaPE_XpfNNwJJlwypeyBFSLvc_DvLDuxdlL3aS47IRfUjZHjZxingSZI2mgk\
        krgr3Kr1jgFoV26z1Suw",
        "authType": 1,
        "inviteSeekId": Encrypt().aes_encrypt("65126515")
    }, {
        "name": "authtype is null,source unknown",
        "phoneNumber": "8021300100",
        "itc": "234",
        "verificationCode": "",
        "verifyType": 0
    }, {
        "name": "phoneNumber is null,login failed",
        "itc": "234",
        "verificationCode": "",
        "authType": 3,
        "verifyType": 0
    }
]
