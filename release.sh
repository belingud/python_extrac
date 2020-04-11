#!/bin/bash
usage() {
    cat <<-USAGE
usage:
$ ./release.sh docker
or:
$ ./release.sh pypi match
>>
USAGE
}

function command_exists() {
    command -v "$@"
}

function read_config() {
    : <<-COMMENT
    read ini suffix file,
    get config block by first argument
    get value of second argument
COMMENT

    file=$1
    block=$2
    item=$3
    val=$(awk -F '\\s=\\s' '/\['${block}'\]/{a=1} (a==1 && "'${item}'"==$1){a=0;print $2}' ${file})
    echo $val
}
function write_config() {
    : <<-COMMENT
    write ini suffix file
COMMENT
    file=$1
    block=$2
    item=$3
    val=$4
    awk -F '\\s=\\s' '/\['${block}'\]/{a=1} (a==1 && "'${item}'"==$1){gsub($2,'${val}');a=0} {print $0}' ${file} 1<>${file}
}

function read_config_block() {
    : <<-COMMENT
    read a block of config file provide by first argument
COMMENT
    file=$1
    val=$(awk '/\[/{printf("%s ",$1)}' ${file} | sed 's/\[//g' | sed 's/\]//g')
    echo ${val}
}

function read_yaml_plus() {
    if [ ! $(command_exists shyaml) ]; then
        echo "you have to install shyaml by 'pip install shyaml' first"
        exit 1
    fi
    image=$(cat $1 | shyaml get-value services.$2.image)
    name=$(echo ${image} | awk -F ':' '{print$1}')
    version=$(echo ${image} | awk -F ':' '{print$2}')
    echo version is $version
    echo $(($(echo ${image} | awk -F ':' '{print$2}' | awk -F '.' '{print$2}') + 1))
}

function build_docker() {
    : <<-COMMENT
    build a docker image named by first argument
    $ build_docker extrac # extrac is docker image name
COMMENT
    docker-compose build $1
}

# config='setup.cfg'
config='docker-compose.yml'
if [ "$1" == "docker" ]; then
    is_docker=true
    is_pypi=false
elif [ "$1" == "pypi" ]; then
    is_docker=false
    is_pypi=true
else
    is_docker=false
    is_pypi=false
    usage
    # exit 1
fi

echo $is_docker
echo $is_pypi

# image_name=$(read_config ${config} docker image)
# echo image name is $image_name

yaml=$(read_yaml_plus ${config} extrac)
echo $yaml

# writeConfig setup.cfg docker current_tag 0.6
# readIniBlock setup.cfg
