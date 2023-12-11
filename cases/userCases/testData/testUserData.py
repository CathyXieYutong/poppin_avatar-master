import base64

blockUserData = [
    {
        "name": "block success",
        "phone": "2348021300101",
        "uid": "65110664"
    }, {
        "name": "user not exist,block failed",
        "phone": "2348021300101",
        "uid": "6511066"
    }, {
        "name": "id is null ,block failed",
        "phone": "2348021300101",
        "uid": ""
    }, {
        "name": "uid is not passed",
        "phone": "2348021300101"
    }, {
        "name": "not login,block failed",
        "uid": "65110664"
    }
]
userStatusData = [
    {
        "name": "query other's profile",
        "phone": "2348021300101",
        "uid": "65184455"
    }, {
        "name": "query self profile",
        "phone": "2348021300101"
    }
]

linkChkData = [
    {
        "phone": "2348021300101",
        "seekId": ""
    }
]

inviteLnkData = [
    {
        "phone": "2348021300102"
    }
]

userProfileData = [
    {
        "phone": "2348021300101",
        "seekId": ""
    }, {
        "phone": "2348021300101",
        "uid": "65184448"
    }

]

userSerchData = [
    {
        "phone": "2348021300100",
        "key": "a"
    }, {
        "phone": "2348021300100",
        "key": "a"
    }, {
        "phone": "2348021300100",
        "key": "azxxzaaazza"
    }, {
        "phone": "2348021300100",
        "key": "2348021300100"
    }
]

userFollowData = [
    {
        "phone": "2348021300101",
        "uid": "65077292"
    }
]