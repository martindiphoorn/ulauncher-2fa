from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

import onetimepass as otp


class TfaExtension(Extension):

    def __init__(self):
        super(TfaExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        data = event.get_argument()
        #### Each token seprate with a space
        providers = extension.preferences.get('tfa_providers').split(" ")

        for provider in providers:
            if data:
                if data not in provider:
                    continue

            secrets = provider.split("=")
            name = secrets[0]
            token = str(otp.get_totp(secrets[1])).zfill(6)

            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s' % token,
                                             description='Provider %s' % name,
                                             on_enter=CopyToClipboardAction(token)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    TfaExtension().run()
