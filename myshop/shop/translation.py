# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product


class CategoryTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Category.
    """

    fields = ('name', 'slug',)


class ProductTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Product.
    """

    fields = ('name', 'slug', 'description',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
