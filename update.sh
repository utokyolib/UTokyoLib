echo "Last Update: $(TZ=-9 date)" > README_new.md
sed -e '1d' README.md >> README_new.md
cp README_new.md README.md
rm README_new.md