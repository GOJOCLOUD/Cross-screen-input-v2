#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
平台工具模块
Mac专用实现
"""

from pynput.keyboard import Key

# Mac专用常量
CURRENT_PLATFORM = 'mac'
IS_WINDOWS = False
IS_MAC = True
IS_LINUX = False


def get_platform():
    """
    检测操作系统平台
    返回: 'mac' (本版本仅支持Mac)
    """
    return 'mac'


def get_modifier_key_map():
    """
    获取Mac平台特定的修饰键映射
    """
    return {
        'ctrl': Key.ctrl,   # Mac 上 ctrl 映射到 Control
        'cmd': Key.cmd,     # cmd 映射到 Command键
        'win': Key.cmd,     # win 也映射到 Command键（兼容性）
        'shift': Key.shift,
        'alt': Key.alt,     # Mac 上 alt 映射到 Option键
    }


# 预加载修饰键映射（避免每次调用都重新创建）
MODIFIER_KEY_MAP = get_modifier_key_map()


__all__ = [
    'get_platform',
    'get_modifier_key_map',
    'CURRENT_PLATFORM',
    'IS_WINDOWS', 
    'IS_MAC',
    'IS_LINUX',
    'MODIFIER_KEY_MAP',
]
