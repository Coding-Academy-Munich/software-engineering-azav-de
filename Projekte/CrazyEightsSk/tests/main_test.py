from crazyeights_sk.__main__ import main


def test_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("Crazy Eights with 2 players:")
    assert "Jack" in captured.out
    assert "Jill" in captured.out
