from shortcut_python_client import ShortcutClient


def test_client_init():
    client = ShortcutClient("test-token")
    assert client._client.headers["Shortcut-Token"] == "test-token"
    client.close()


def test_client_context_manager():
    with ShortcutClient("test-token") as client:
        assert client._client.headers["Shortcut-Token"] == "test-token"
