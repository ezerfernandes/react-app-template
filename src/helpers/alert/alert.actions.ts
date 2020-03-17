import { alertConstants } from './alert.constants';

export const alertActions = {
    success, error, clear
}

function success(message: string) {
    return { type: alertConstants.SUCCESS, message: message }
}

function error(message: string) {
    return { type: alertConstants.ERROR, message: message }
}

function clear() {
    return { type: alertConstants.CLEAR }
}