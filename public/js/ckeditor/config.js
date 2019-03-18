/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
  // Define changes to default configuration here. For example:
  config.language = 'zh-cn';
  config.allowedContent = true;
  config.toolbar_Full = [
    ['Underline', '-', 'Subscript', 'Superscript', 'RemoveFormat'],
    ['Image', 'Table', 'SpecialChar'],
    ['ckeditor_wiris_formulaEditor']
  ]; // 配置工具条
  config.width = 360; // 编辑器宽度设置
  config.resize_enabled = false;
};
