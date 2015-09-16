#!/bin/bash

SYS_DEPS=(python-pip python-setuptools python-devel gcc make gcc-c++ MySQL-python)
PYTHON_DEPS=(paramiko fabric)

function install_dependencies(){
  echo "Installing required system packages..."
  for sys_dep in ${SYS_DEPS[@]}; do
    install_sys_dep $sys_dep
  done

  echo "Installing required python packages..."
  for python_dep in ${PYTHON_DEPS[@]}; do
    install_python_dep ${python_dep}
  done
}

function install_sys_dep(){         
  if [[ $(rpm -q ${1} |grep -wc "not") = 1 ]]; then
    yum -y -q install  $1
  else
    echo "Package \"${1}\" was already installed."
  fi
}

function install_python_dep(){                          
  if [[ $(python-pip freeze |grep -wc "${1}") = 0 ]]; then
    python-pip -q install $1
  else
    echo "Python package \"${1}\" was already installed."
  fi
}

install_dependencies
