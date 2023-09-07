import { Component } from '@angular/core';

@Component({
  selector: 'app-powerbi',
  templateUrl: './powerbi.component.html',
  styleUrls: ['./powerbi.component.css']
})
export class PowerbiComponent {
  openPowerBIReport() {
    const powerBIReportUrl = 'https://app.powerbi.com/groups/me/reports/64fa5cb0-a1df-4666-ab46-e44efba400a5/ReportSection';
    window.open(powerBIReportUrl, '_blank');
  }

}
