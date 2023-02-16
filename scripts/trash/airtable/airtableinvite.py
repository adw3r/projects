import json
from os.path import basename

import requests

import module
from module import Spam


def delete(s, inviteId):
    cookies = {
        '_gcl_au': '1.1.313778930.1675071403',
        '_ga': 'GA1.2.1706294687.1675071403',
        '_pxvid': 'f508efe8-a216-11ed-b07e-7657574f5455',
        'optimizelyEndUserId': 'oeu1675329111172r0.5439660237219517',
        '_mkto_trk': 'id:458-JHQ-131&token:_mch-airtable.com-1675329111502-42943',
        '_fbp': 'fb.1.1675329129729.1912590730',
        '_gid': 'GA1.2.914263093.1676545072',
        'mv': 'eyJzdGFydFRpbWUiOiIyMDIzLTAyLTE2VDEwOjU3OjU4LjI2M1oiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tLyIsImludGVybmFsVHJhY2VJZCI6InRyY1pBZkd3WjVBR2NqWEkyIn0=',
        'pxcts': '6fd12ea5-adf4-11ed-8f1f-786f6c735078',
        'lithiumSSO:': '~2tvTOz3RkhJSfpy4x~HNuOv5jG71ijvQhCjKWy1lBicpijreA_aEBC2ymd_b5JT-d7_uNAt4Sp53FD-JoojRJG9dQDoyKCWJi9-TKqzq3clhHWHhDvy61GUu9iGzszjjN0IbTrkJmQ77d320JOwmju0M0k3Do4SWwozbkfMc7BYHT4g4Q-AWgGHaOPna9eaUyoeAm3L36je0O1nqzJEW7g91G3lgqohwRDXW-8u7QGpT4WvFJvkuJHvaU3KdTzXREc8EfC33x-bh5aeC_7pg5PWCF2lkMadu0RjNfTVOC6Os6IuQtIVYwP86I2P2LW2ECjbbqkzkG8uQtI5-Z-krsdH4HIR1IXVlLEPrbOKA..',
        'amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com': 'eyJkZXZpY2VJZCI6ImNmNWVhMzYwLTQ5NmYtNDM0MC05M2E0LTBlMTdlZjFjYjlhNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjU1MDA3MDgxNCwibGFzdEV2ZW50VGltZSI6MTY3NjU1MDMxMDQxOSwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjN9',
        'brw': 'brwYDKP4mmWCrfZJK',
        'login-status-p': '1',
        'localePref': 'auto',
        '__Host-airtable-session': 'eyJzZXNzaW9uSWQiOiJzZXNYQkdvN0tlNVJjSWFuNiIsImNzcmZTZWNyZXQiOiI0S2FfVmdPMGVKVXdQQ2ZyUk0wa213blQiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzY1NTAzMjQ2MzMsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0xNlQxMjoyNToyNC43NDJaIn0=',
        '__Host-airtable-session.sig': 'CDb8vmV2wZ7qFtoeF2pLHvZEV64DLgZIZKy9sBiyqEQ',
        'userSignature': 'usrvgYwOGDFbzGoDQ2023-02-16T12:36:00.000Z',
        'userSignature.sig': 'k2PVshOEtgQYJrg-Q0X3vXm6wD2ixoSAqFFH1WLfCmg',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+16+2023+14%3A36%3A02+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=3eacbd10-1648-4cd2-b5aa-cbefb7582937&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
        '_gat_UA-183354518-1': '1',
        '_uetsid': 'c27e3320ade811ed9362cff633ab58ed',
        '_uetvid': '9b22e740a08111edaca9ada90411b9dc',
        'AWSALB': 'DrPJz/q8cbOSb+ivN5teR7nolZ41xcKp4Cpp9xXbE8EQnAKxMOyb7ww6bl0Vo9lMPMF+clLkgeEb1QI9yPj+bDcB1kDfKyYXFjpm0UFns84Xacz6+k+dqqzb8Y1L',
        'AWSALBCORS': 'DrPJz/q8cbOSb+ivN5teR7nolZ41xcKp4Cpp9xXbE8EQnAKxMOyb7ww6bl0Vo9lMPMF+clLkgeEb1QI9yPj+bDcB1kDfKyYXFjpm0UFns84Xacz6+k+dqqzb8Y1L',
        'mbpg': '2024-02-16T12:36:48.035ZusrvgYwOGDFbzGoDQpro',
        'mbpg.sig': 'iCrPdITj0WvOcJYm-pqTdRY-f1dLIMsp699TWTiv_Zk',
    }

    headers = {
        'authority': 'airtable.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.313778930.1675071403; _ga=GA1.2.1706294687.1675071403; _pxvid=f508efe8-a216-11ed-b07e-7657574f5455; optimizelyEndUserId=oeu1675329111172r0.5439660237219517; _mkto_trk=id:458-JHQ-131&token:_mch-airtable.com-1675329111502-42943; _fbp=fb.1.1675329129729.1912590730; _gid=GA1.2.914263093.1676545072; mv=eyJzdGFydFRpbWUiOiIyMDIzLTAyLTE2VDEwOjU3OjU4LjI2M1oiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tLyIsImludGVybmFsVHJhY2VJZCI6InRyY1pBZkd3WjVBR2NqWEkyIn0=; pxcts=6fd12ea5-adf4-11ed-8f1f-786f6c735078; lithiumSSO:=~2tvTOz3RkhJSfpy4x~HNuOv5jG71ijvQhCjKWy1lBicpijreA_aEBC2ymd_b5JT-d7_uNAt4Sp53FD-JoojRJG9dQDoyKCWJi9-TKqzq3clhHWHhDvy61GUu9iGzszjjN0IbTrkJmQ77d320JOwmju0M0k3Do4SWwozbkfMc7BYHT4g4Q-AWgGHaOPna9eaUyoeAm3L36je0O1nqzJEW7g91G3lgqohwRDXW-8u7QGpT4WvFJvkuJHvaU3KdTzXREc8EfC33x-bh5aeC_7pg5PWCF2lkMadu0RjNfTVOC6Os6IuQtIVYwP86I2P2LW2ECjbbqkzkG8uQtI5-Z-krsdH4HIR1IXVlLEPrbOKA..; amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com=eyJkZXZpY2VJZCI6ImNmNWVhMzYwLTQ5NmYtNDM0MC05M2E0LTBlMTdlZjFjYjlhNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjU1MDA3MDgxNCwibGFzdEV2ZW50VGltZSI6MTY3NjU1MDMxMDQxOSwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjN9; brw=brwYDKP4mmWCrfZJK; login-status-p=1; localePref=auto; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNYQkdvN0tlNVJjSWFuNiIsImNzcmZTZWNyZXQiOiI0S2FfVmdPMGVKVXdQQ2ZyUk0wa213blQiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzY1NTAzMjQ2MzMsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0xNlQxMjoyNToyNC43NDJaIn0=; __Host-airtable-session.sig=CDb8vmV2wZ7qFtoeF2pLHvZEV64DLgZIZKy9sBiyqEQ; userSignature=usrvgYwOGDFbzGoDQ2023-02-16T12:36:00.000Z; userSignature.sig=k2PVshOEtgQYJrg-Q0X3vXm6wD2ixoSAqFFH1WLfCmg; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+16+2023+14%3A36%3A02+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=3eacbd10-1648-4cd2-b5aa-cbefb7582937&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _gat_UA-183354518-1=1; _uetsid=c27e3320ade811ed9362cff633ab58ed; _uetvid=9b22e740a08111edaca9ada90411b9dc; AWSALB=DrPJz/q8cbOSb+ivN5teR7nolZ41xcKp4Cpp9xXbE8EQnAKxMOyb7ww6bl0Vo9lMPMF+clLkgeEb1QI9yPj+bDcB1kDfKyYXFjpm0UFns84Xacz6+k+dqqzb8Y1L; AWSALBCORS=DrPJz/q8cbOSb+ivN5teR7nolZ41xcKp4Cpp9xXbE8EQnAKxMOyb7ww6bl0Vo9lMPMF+clLkgeEb1QI9yPj+bDcB1kDfKyYXFjpm0UFns84Xacz6+k+dqqzb8Y1L; mbpg=2024-02-16T12:36:48.035ZusrvgYwOGDFbzGoDQpro; mbpg.sig=iCrPdITj0WvOcJYm-pqTdRY-f1dLIMsp699TWTiv_Zk',
        'origin': 'https://airtable.com',
        'referer': 'https://airtable.com/appnK7yQpRh4Anki4/tblQaMOEOwGa6yznA/viwnB3EIg1TtDS6jn?blocks=hide',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-airtable-application-id': 'appnK7yQpRh4Anki4',
        'x-airtable-client-queue-time': '2',
        'x-airtable-inter-service-client': 'webClient',
        'x-airtable-inter-service-client-code-version': '8e70e695539ba336b191d0a337962343a932083d',
        'x-airtable-page-load-id': 'pglISf3soYUhTL71Y',
        'x-requested-with': 'XMLHttpRequest',
        'x-time-zone': 'Europe/Kiev',
        'x-user-locale': 'en',
    }

    data = {
        'stringifiedObjectParams': '{"collaboratorModelIds":["inviteId"]}',
        'requestId': 'reqYGNIS2URre1WvK',
        'secretSocketId': 'soc6qeCebknrbstld',
    }

    data['stringifiedObjectParams'] = data['stringifiedObjectParams'].replace('inviteId', inviteId)
    data['requestId'] = f'req{module.generate_text(14)}'

    response = s.post(
        'https://airtable.com/v0.3/application/appnK7yQpRh4Anki4/bulkUnshare',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response


def invite(s, target, text):
    cookies = {
        '_gcl_au': '1.1.313778930.1675071403',
        '_ga': 'GA1.2.1706294687.1675071403',
        '_pxvid': 'f508efe8-a216-11ed-b07e-7657574f5455',
        'optimizelyEndUserId': 'oeu1675329111172r0.5439660237219517',
        '_mkto_trk': 'id:458-JHQ-131&token:_mch-airtable.com-1675329111502-42943',
        '_fbp': 'fb.1.1675329129729.1912590730',
        '_gid': 'GA1.2.914263093.1676545072',
        'mv': 'eyJzdGFydFRpbWUiOiIyMDIzLTAyLTE2VDEwOjU3OjU4LjI2M1oiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tLyIsImludGVybmFsVHJhY2VJZCI6InRyY1pBZkd3WjVBR2NqWEkyIn0=',
        'pxcts': '6fd12ea5-adf4-11ed-8f1f-786f6c735078',
        'lithiumSSO:': '~2tvTOz3RkhJSfpy4x~HNuOv5jG71ijvQhCjKWy1lBicpijreA_aEBC2ymd_b5JT-d7_uNAt4Sp53FD-JoojRJG9dQDoyKCWJi9-TKqzq3clhHWHhDvy61GUu9iGzszjjN0IbTrkJmQ77d320JOwmju0M0k3Do4SWwozbkfMc7BYHT4g4Q-AWgGHaOPna9eaUyoeAm3L36je0O1nqzJEW7g91G3lgqohwRDXW-8u7QGpT4WvFJvkuJHvaU3KdTzXREc8EfC33x-bh5aeC_7pg5PWCF2lkMadu0RjNfTVOC6Os6IuQtIVYwP86I2P2LW2ECjbbqkzkG8uQtI5-Z-krsdH4HIR1IXVlLEPrbOKA..',
        'amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com': 'eyJkZXZpY2VJZCI6ImNmNWVhMzYwLTQ5NmYtNDM0MC05M2E0LTBlMTdlZjFjYjlhNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjU1MDA3MDgxNCwibGFzdEV2ZW50VGltZSI6MTY3NjU1MDMxMDQxOSwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjN9',
        'brw': 'brwYDKP4mmWCrfZJK',
        'login-status-p': '1',
        'localePref': 'auto',
        '__Host-airtable-session': 'eyJzZXNzaW9uSWQiOiJzZXNYQkdvN0tlNVJjSWFuNiIsImNzcmZTZWNyZXQiOiI0S2FfVmdPMGVKVXdQQ2ZyUk0wa213blQiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzY1NTAzMjQ2MzMsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0xNlQxMjoyNToyNC43NDJaIn0=',
        '__Host-airtable-session.sig': 'CDb8vmV2wZ7qFtoeF2pLHvZEV64DLgZIZKy9sBiyqEQ',
        'userSignature': 'usrvgYwOGDFbzGoDQ2023-02-16T12:36:00.000Z',
        'userSignature.sig': 'k2PVshOEtgQYJrg-Q0X3vXm6wD2ixoSAqFFH1WLfCmg',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+16+2023+14%3A36%3A02+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=3eacbd10-1648-4cd2-b5aa-cbefb7582937&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
        '_gat_UA-183354518-1': '1',
        '_uetsid': 'c27e3320ade811ed9362cff633ab58ed',
        '_uetvid': '9b22e740a08111edaca9ada90411b9dc',
        'AWSALB': 'krJLRzkvtNfbgiHh6Wib7WP1iybIHnRig6c+En3ZqU+6hCTd4c1tTYiDg4f4jkLsP8Po3vU1LHGvi/zTU+qpKa08enA+aUHw2ct2M4HvZrFd5JmMLob8oQVTrPtU',
        'AWSALBCORS': 'krJLRzkvtNfbgiHh6Wib7WP1iybIHnRig6c+En3ZqU+6hCTd4c1tTYiDg4f4jkLsP8Po3vU1LHGvi/zTU+qpKa08enA+aUHw2ct2M4HvZrFd5JmMLob8oQVTrPtU',
        'mbpg': '2024-02-16T12:36:29.056ZusrvgYwOGDFbzGoDQpro',
        'mbpg.sig': 'EtwKff4Q0hGYZWrCP6xoAeDRG8TlpbLiyc1830ujDjM',
    }

    headers = {
        'authority': 'airtable.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.313778930.1675071403; _ga=GA1.2.1706294687.1675071403; _pxvid=f508efe8-a216-11ed-b07e-7657574f5455; optimizelyEndUserId=oeu1675329111172r0.5439660237219517; _mkto_trk=id:458-JHQ-131&token:_mch-airtable.com-1675329111502-42943; _fbp=fb.1.1675329129729.1912590730; _gid=GA1.2.914263093.1676545072; mv=eyJzdGFydFRpbWUiOiIyMDIzLTAyLTE2VDEwOjU3OjU4LjI2M1oiLCJsb2NhdGlvbiI6Imh0dHBzOi8vYWlydGFibGUuY29tLyIsImludGVybmFsVHJhY2VJZCI6InRyY1pBZkd3WjVBR2NqWEkyIn0=; pxcts=6fd12ea5-adf4-11ed-8f1f-786f6c735078; lithiumSSO:=~2tvTOz3RkhJSfpy4x~HNuOv5jG71ijvQhCjKWy1lBicpijreA_aEBC2ymd_b5JT-d7_uNAt4Sp53FD-JoojRJG9dQDoyKCWJi9-TKqzq3clhHWHhDvy61GUu9iGzszjjN0IbTrkJmQ77d320JOwmju0M0k3Do4SWwozbkfMc7BYHT4g4Q-AWgGHaOPna9eaUyoeAm3L36je0O1nqzJEW7g91G3lgqohwRDXW-8u7QGpT4WvFJvkuJHvaU3KdTzXREc8EfC33x-bh5aeC_7pg5PWCF2lkMadu0RjNfTVOC6Os6IuQtIVYwP86I2P2LW2ECjbbqkzkG8uQtI5-Z-krsdH4HIR1IXVlLEPrbOKA..; amplitude_id_01c5c9182d4beaee719619af5db39310airtable.com=eyJkZXZpY2VJZCI6ImNmNWVhMzYwLTQ5NmYtNDM0MC05M2E0LTBlMTdlZjFjYjlhNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjU1MDA3MDgxNCwibGFzdEV2ZW50VGltZSI6MTY3NjU1MDMxMDQxOSwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjN9; brw=brwYDKP4mmWCrfZJK; login-status-p=1; localePref=auto; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNYQkdvN0tlNVJjSWFuNiIsImNzcmZTZWNyZXQiOiI0S2FfVmdPMGVKVXdQQ2ZyUk0wa213blQiLCJoaWdoU2VjdXJpdHlNb2RlRW5hYmxlZFRpbWUiOjE2NzY1NTAzMjQ2MzMsInVzZXJJZCI6InVzcnZnWXdPR0RGYnpHb0RRIiwibG9nZ2VkSW5UaW1lIjoiMjAyMy0wMi0xNlQxMjoyNToyNC43NDJaIn0=; __Host-airtable-session.sig=CDb8vmV2wZ7qFtoeF2pLHvZEV64DLgZIZKy9sBiyqEQ; userSignature=usrvgYwOGDFbzGoDQ2023-02-16T12:36:00.000Z; userSignature.sig=k2PVshOEtgQYJrg-Q0X3vXm6wD2ixoSAqFFH1WLfCmg; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+16+2023+14%3A36%3A02+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=3eacbd10-1648-4cd2-b5aa-cbefb7582937&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _gat_UA-183354518-1=1; _uetsid=c27e3320ade811ed9362cff633ab58ed; _uetvid=9b22e740a08111edaca9ada90411b9dc; AWSALB=krJLRzkvtNfbgiHh6Wib7WP1iybIHnRig6c+En3ZqU+6hCTd4c1tTYiDg4f4jkLsP8Po3vU1LHGvi/zTU+qpKa08enA+aUHw2ct2M4HvZrFd5JmMLob8oQVTrPtU; AWSALBCORS=krJLRzkvtNfbgiHh6Wib7WP1iybIHnRig6c+En3ZqU+6hCTd4c1tTYiDg4f4jkLsP8Po3vU1LHGvi/zTU+qpKa08enA+aUHw2ct2M4HvZrFd5JmMLob8oQVTrPtU; mbpg=2024-02-16T12:36:29.056ZusrvgYwOGDFbzGoDQpro; mbpg.sig=EtwKff4Q0hGYZWrCP6xoAeDRG8TlpbLiyc1830ujDjM',
        'origin': 'https://airtable.com',
        'referer': 'https://airtable.com/appnK7yQpRh4Anki4/tblQaMOEOwGa6yznA/viwnB3EIg1TtDS6jn?blocks=hide',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-airtable-application-id': 'appnK7yQpRh4Anki4',
        'x-airtable-client-queue-time': '2.5',
        'x-airtable-inter-service-client': 'webClient',
        'x-airtable-inter-service-client-code-version': '8e70e695539ba336b191d0a337962343a932083d',
        'x-airtable-page-load-id': 'pglISf3soYUhTL71Y',
        'x-requested-with': 'XMLHttpRequest',
        'x-time-zone': 'Europe/Kiev',
        'x-user-locale': 'en',
    }

    data = {
        'stringifiedObjectParams': json.dumps(
            {"emails": [target, target, target, target, target], "groupIds": [], "permissionLevel": "read",
             "message": 'www.google.com', "shareEntrypoint": "mention_suggest"}),
        'requestId': f'req{module.generate_text(14)}',
        'secretSocketId': 'socXq8jqRHBB1NdVZ',
    }

    response = s.post(
        'https://airtable.com/v0.3/application/appnK7yQpRh4Anki4/multiShareAndInvite',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response


class ConcreteSpam(Spam):
    attempts = 30

    def post(self, target) -> requests.Response | None:
        s = requests.Session()
        s.proxies = self.get_proxies()
        inv_resp = invite(s, target, self.get_text())
        print(inv_resp.text)
        inv_resp_json = inv_resp.json()
        inv_resp_json_data_ = inv_resp_json['data']
        target_ = inv_resp_json_data_[target]
        inviteId = target_.get('inviteId')
        if not inviteId:
            return
        del_resp = delete(s, inviteId)
        print(del_resp.text)
        return del_resp


def main():
    spam = ConcreteSpam(basename(__file__).removesuffix('.py'))
    res = spam.send_post('softumwork@gmail.com')
    # if res:
    #     spam.run_concurrently()


if __name__ == '__main__':
    main()
