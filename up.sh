
cd `dirname $0`

git add . --sparse
git commit -am update
git push
