import request from '@/utils/request'

export function getTableSettingApi(page) {
  return request({
    url: '/system/table-setting/' + encodeURIComponent(page),
    method: 'get'
  })
}

export function saveTableSettingApi(page, setting) {
  return request({
    url: '/system/table-setting',
    method: 'post',
    data: { page, setting }
  })
}
