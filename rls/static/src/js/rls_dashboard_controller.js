odoo.define('request_legal_services.rls_dashboard_controller', function (require) {
    'use strict';

    const AbstractController = require('web.AbstractController');
    const core = require('web.core');
    const _t = core._t;

    class RlSDashboardController extends AbstractController {

        on_attach_callback() {
            this._loadDashboardData();
        }

        async _loadDashboardData() {
            // Fetch data for the dashboard
            const data = await this._rpc({
                route: '/rls/data',
            });

            // Initialize the charts
            this._initOpenRequestsChart(data.open_requests);
            this._initWeeklyRequestsChart(data.weekly_requests);
        }

        _initOpenRequestsChart(openRequestsData) {
            // Create a doughnut chart for the open requests per attorney
            const openRequestsCtx = this.$('#open-requests-chart')[0].getContext('2d');
            new Chart(openRequestsCtx, {
                type: 'doughnut',
                data: {
                    labels: openRequestsData.map(item => item.attorney_name),
                    datasets: [{
                        data: openRequestsData.map(item => item.open_requests),
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'], // Add more colors if needed
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: _t('Open Requests per Attorney'),
                    },
                },
            });
        }

        _initWeeklyRequestsChart(weeklyRequestsData) {
            // Create a bar chart for the new requests per day of the current week
            const weeklyRequestsCtx = this.$('#weekly-requests-chart')[0].getContext('2d');
            new Chart(weeklyRequestsCtx, {
                type: 'bar',
                data: {
                    labels: weeklyRequestsData.map(item => item.day),
                    datasets: [{
                        label: _t('New Requests'),
                        data: weeklyRequestsData.map(item => item.new_requests),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                            },
                        }],
                    },
                    title: {
                        display: true,
                        text: _t('New Requests per Day of the Current Week'),
                    },
                },
            });
        }
    }

    return RlSDashboardController;
});
