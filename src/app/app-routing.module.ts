import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { PredictionComponent } from './components/prediction/prediction.component';
import { ResultsComponent } from './components/results/results.component';
import { GraphComponent } from './components/graph/graph.component';
import { HomeComponent } from './components/home/home.component';
import { IndexComponent } from './components/index/index.component';
import { PowerbiComponent } from './components/powerbi/powerbi.component';

const routes: Routes = [
  {path:'',redirectTo:'index', pathMatch:'full'},
  {path:'register' ,component:RegisterComponent},
  {path:'login' ,component:LoginComponent},
  {path: 'home', component: HomeComponent },
  {path:'prediction' , component:PredictionComponent},
  {path:'graph' , component:GraphComponent},
  {path:'results' , component:ResultsComponent},
  {path:'index' , component:IndexComponent},
  {path:'powerbi' , component:PowerbiComponent},

  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
