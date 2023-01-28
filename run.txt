pytest -v --html=Reports\report.html
rem pytest -v --browser chrome --html=Reports\report.html
rem pytest -v --browser edge --html=Reports\report.html
rem pytest -v -m "sanity" --html=Reports\report.html
rem pytest -v -m "regression" --html=Reports\report.html
rem pytest -v -m "smoke" --html=Reports\report.html
rem pytest -v -m "sanity and smoke" --html=Reports\report.html
rem pytest -v -m "sanity and regression" --html=Reports\report.html
rem pytest -v -s -n=3 --html=Reports\report.html