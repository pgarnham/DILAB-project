Rails.application.routes.draw do
  devise_for :users
  root 'home#index'
  get 'home/data_heatmap'
  get 'home/visualizacion'
  get 'home/data1'
  get 'home/data2'
  get 'home/data3'
  get 'home/data4'
  get 'home/data5'
  get 'home/data6'
  get 'home/data7'
  get 'home/data8'
  get 'home/data9'
  get 'home/data10'
  get 'home/data'
  get 'home/day_hour'
  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
