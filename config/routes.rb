Rails.application.routes.draw do
  devise_for :users
  root 'home#index'
  get 'home/data_heatmap'
  get 'home/visualizacion'
  get 'home/data2'
  get 'home/data'
  get 'home/day_hour'
  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
